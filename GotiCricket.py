from Cricket_navam import *
from keys import *
import telebot

url_comm = 'https://www.cricbuzz.com/live-cricket-scores/33810/eng-vs-nz-2nd-test-new-zealand-tour-of-england-2021'
url = 'https://www.cricbuzz.com/live-cricket-scorecard/33810/eng-vs-nz-2nd-test-new-zealand-tour-of-england-2021'
cric = Cricket(url_comm, url)
cric.get_playing_11()
API_KEY = API_KEY_SECRET
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message,"Hey!!! This bot is created by Bhavesh and Navam")


@bot.message_handler(commands=['score'])
def score(message):
	

	cric.Update()

	bot.reply_to(message,cric.get_curr_team_score())
	bot.reply_to(message, '\n'.join(cric.get_playing_bats()))
	bot.reply_to(message,cric.get_playing_bowl())


bot.polling()	