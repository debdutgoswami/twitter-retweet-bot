import twitterbot as tb
import secrets
import sys

hashtag = sys.argv[1]

credintials = secrets.get_credentials()

bot = tb.Twitterbot(credintials['email'], credintials['password'])
bot.login()
bot.like_retweet(hashtag)