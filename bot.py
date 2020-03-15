import pprint
import zulip
import sys
import re
import json
import httplib2
import os
from pnr import Pnr

p = pprint.PrettyPrinter()
BOT_MAIL = "bot@yourbot.zulipchat.com"

class ZulipBot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://yourbot.zulipchat.com/api/")
		self.subscribe_all()
		self.chatbot = ChatBot("Trainwala", trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
		self.chatbot.train("chatterbot.corpus.english")	
    	self.pnr = Pnr() 
		self.subkeys = [ "pnr"]

	def urls(self, link):
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link)
		return urls

	def subscribe_all(self):
		json = self.client.get_streams()["streams"]
		streams = [{"name": stream["name"]} for stream in json]
		self.client.add_subscriptions(streams)

	def help(self):
		message = "**Welcome to Trainwala Bot**\nTrainwala Bot has Trains pnr info .\n"
		message += "`pnr` - Get PNR Status\n"
		return message
	def help_sub(self, key):
		key = key.lower()
		message = "**Usage**\n"
		if key == "pnr":
			message += "`Trainwala pnr <valid pnr number>` - Get PNR Details of the Given PNR number\n"
		else:
			message = self.help()
			message += "\n{} is not a valid \n".format(key)
		return message		

	def process(self, msg):
		content = msg["content"].split()
		sender_email = msg["sender_email"]
		ttype = msg["type"]
		stream_name = msg['display_recipient']
		stream_topic = msg['subject']

		print(content)

		if sender_email == BOT_MAIL:
			return 

		print("yeah")

		if content[0].lower() == "Trainwala" or content[0] == "@**Trainwala**":
			if content[1].lower() == "pnr":
				message = self.pnr.get_pnr(content[2])
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})

		elif "Trainwala" in content and content[0] != "Trainwala":
			self.client.send_message({
				"type": "stream",
				"subject": msg["subject"],
				"to": msg["display_recipient"],
				"content": "Alas! Finally you called me :blush:"
				})
		else:
			return
			
def main():
	bot = ZulipBot()
	bot.client.call_on_each_message(bot.process)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Thanks for using Trainwala Bot. Bye!")
		sys.exit(0)