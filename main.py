import twitterbot as tb
import secrets
import sys

hashtag = sys.argv[1]

bot = tb.Twitterbot(secrets.email, secrets.password)
bot.login()
bot.retweet(hashtag)