# Trainwala-bot-zulip
A live train PNR app that gives information about bookings and confirmations of train

## Setup
Run the following commands from Your root directory

## Step 1

`https://github.com/spielers/Trainwala-bot-zulip.git`  /* To clone this repository */

`cd Trainwala-bot-zulip ` /* To Navigate to the cloned repo */

`git clone https://github.com/zulip/python-zulip-api.git` /* To installling zulip environment */

`cd python-zulip-api` - navigate into your cloned repository.

`python3 ./tools/provision` - install all requirements in a Python virtualenv.

The output of provision will end with a command of the form source .../activate; run that command to enter the new virtualenv. 


## Step 2 

Go to your Zulip account and add a bot. Use Generic bot as the bot type.

Download the bot's `zuliprc` configuration file to your computer.

Download the `zulip_bots` Python package to your computer using `pip3 install zulip_bots`.

## step 3
Install all the requirements using ` pip install -r requirements.txt`

In bot.py file replace the site in self.client = zulip.Client(site="https://yourbot.zulipchat.com/api/") to url of your created zulip realm. Do the same for BOT_MAIL variable add the name that you set before.

`python3 bot.py` to run the bot 

## To Start the bot process on your computer.

`Run zulip-run-bot <bot-name> --config-file ~/path/to/zuliprc`
here replace bot name with the generic bot that you created in zulip application above and give the correct path to the zulpric that you have downloaded.
