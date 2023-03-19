import src.message, src.config, src.utility
import pathlib, asyncio, time
from telethon import TelegramClient, events
from telethon.errors import ConnectionError

api_id = int(src.config.value_get("TELAUTH", "api_id"))
api_hash = src.config.value_get("TELAUTH", "api_hash")
group_id = src.config.value_get("TELAUTH", "group_id")
session = str(pathlib.Path(__file__).parents[1] / "data/session_file.session")

client = TelegramClient(session, api_id, api_hash)

##### ------------------------------------------------------------ #####
                    # support functions #
##### ------------------------------------------------------------ #####

async def _disconnect_client():
    src.utility.log_it("disconnecting the event listener")
    src.utility.log_write()
    client.disconnect()
    exit(0)

async def _clear_messages():
    try:
        messages = await client.get_messages(entity = group_id)
        await client.delete_messages(entity = group_id, message_ids = messages)

    except Exception as e:
        src.utility.log_it(f"exception occured in the event listener: {e}")
        src.utility.log_write()

        src.utility.lock_set(False)

        client.disconnect()
        loop = asyncio.get_running_loop()
        loop.stop()

async def _send_message(msg):
    await asyncio.sleep(3)
    await client.send_message(entity = group_id, message = msg)

@client.on(events.NewMessage())
async def handler(event):
    msg = event.message.message
    # print(f"message received: {msg}")
    
    if not src.utility.lock():
            src.utility.lock_set(True)
            src.utility.log_it(f"message gathered and forwarded, msg: {msg}")
            src.message.parse_message(msg)
    else:
        # src.utility.log_it(f"not forwarded lock!, message:\n\n{msg}")
        # src.utility.log_write()
        src.utility.lock_set(False)

##### ------------------------------------------------------------ #####
                    # callable funcitons #
##### ------------------------------------------------------------ #####

def send_message(message):
    src.utility.log_write()
    loop = asyncio.get_running_loop()
    asyncio.run_coroutine_threadsafe(_send_message(message), loop)

def clear_chat():
    task = asyncio.create_task(_clear_messages())
    asyncio.wait([task])
    # loop = asyncio.get_running_loop()
    # asyncio.run(_clear_messages(), loop)

def stop_bot():
    loop = asyncio.get_running_loop()
    asyncio.run_coroutine_threadsafe(_disconnect_client(), loop)

def run():
    src.utility.log_it("connecting the event listener to the chat with telethon")
    src.utility.log_write()

    try:
        client.start()
        client.run_until_disconnected()

    except Exception as e:
        src.utility.log_it(f"During the listening for new messages an Exception occured: {e}")
        src.utility.log_it(f"waiting 5 seconds and try to reconnect")
        src.utility.log_write()

        time.sleep(5)
        run()