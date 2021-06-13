from Cricket_navam import *
from keys import *
import telebot

url_comm = 'https://www.cricbuzz.com/live-cricket-scores/33810/eng-vs-nz-2nd-test-new-zealand-tour-of-england-2021'
url = 'https://www.cricbuzz.com/live-cricket-scorecard/33810/eng-vs-nz-2nd-test-new-zealand-tour-of-england-2021'

cric = Cricket(url_comm, url)
cric.get_playing_11()

secret = Secret()
API_KEY = secret.API_KEY_SECRET
welcome_msg = secret.WelcomeMessage

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message,welcome_msg)


@bot.message_handler(commands=['score'])
def score(message):
	

	cric.Update()

	score = cric.get_curr_team_score()
	batsman = '\n'.join(cric.get_playing_bats())
	bowler = cric.get_playing_bowl()

	preview = score + "\n" + batsman + "\n" + bowler
	bot.reply_to(message,preview)

@bot.message_handler(commands=['scorecard'])
def scorecard(message):

	cric.Update()

	score_board = cric.get_score_board()

	
	bot.reply_to(message,score_board)


bot.polling()	