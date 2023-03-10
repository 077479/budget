# Balance Book Script for Telegram
- python dependent tool to manage weekly expenses

# Install
## Requirements
- **git** 2.37.3
- **python** 3.10.7
- **telethon** 1.26.0

## Virtual Environment
- **create a virtual environment**:
    - ``python -m venv env_habit_tracker``
    - ``cd env_habit_tracker``
- **activate the virtual environment**:
    - **Windows**:
        - ``.\Scripts\activate``
    - **Linux**:
        - ``./bin/activate``
> to deactivate just type ``deactivate``

## Clone
- **clone the repo from github**:
    - ``git clone https://github.com/077479/ledger.git``

## Install
- windows:
    - ``cd ledger\wheel``
- Linux:
    - ``cd ledger/wheel``
- **install with pip**:
    - ``pip install habtrack-1.0-py3-none-any.whl``

# Usage
## before usage
- the tool has to be connected to telegram through a "api_id" and api_hash
- the telegram group_id is used to connect to the specific group
- the tool will try to access the file ``project_root/data/tincan.py``
- this file has the blank variables for ``api_id``, ``api_hash`` and ``group_id``
- this variables has to be set mannually!

## Set Vars
- the variables are set through cli_calls
- **api_id**:
    - ``ledger.set_var api_id [value]``
    - ``ledger.set_var api_hash [value]``
    - ``ledger.set_var group_id [value]``

## General
- the tool will scan the group for specific messages that represents commands
- the idea is that a weekly amount can be set as expensable income
- everytime an expense is made the expense will be send as message into the chat
- the form of the eypense has to be ``xx,yy`` or ``xx`` (xx for the amount before the separator)
- the tool will store the expense and automatically subtract the amount from the weekly amount
- to start the tool use: ``ledger.start``

## Commands
- ``balance``
    - shows the actual balance
    - should not be neccessary because teh tool will always provide this
- ``week``
    - shows the expenses for the actual week
- ``revoke``
    - revokes the last expenses
- ``set_balance``
    - sets the weekly balance