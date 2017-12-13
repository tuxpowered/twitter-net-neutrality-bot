#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*** THIS IS PROVIDED AS IS, USE RESPONSIBLY ****

"""

import tweepy
import random
import retry
import logging
from time import sleep


consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
tweet_delay = 300       # How many seconds to wait between tweets

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler=auth)

#https://www.battleforthenet.com/breaktheinternet/?org=dp#tweets
tweets = [
    "WE HAVE *JUST* 48 HOURS TO #STOPTHEFCC and save the Internet. Take action now and spread the word: battleforthenet.com",
    "#NetNeutrality dies in 2 days unless we stop this."
    "Contact Congress now: battleforthenet.com"  
    "Contact Congress now: battleforthenet.com"
    "Contact Congress now: battleforthenet.com"
    "Contact Congress now: battleforthenet.com",

    "#NetNeutrality dies in 2 days unless we stop this."
    "Call Congress now: 202-759-7766"
    "Call Congress now: 202-759-7766"
    "Call Congress now: 202-759-7766"
    "Call Congress now: 202-759-7766"
    "Call Congress now: 202-759-7766"
    "Call Congress now: 202-759-7766"
    "Call Congress now: 202-759-7766",

    "Everyone needs to know that Congress has stopped FCC votes before. They can stop Ajit Pai’s plan and save #netneutrality. Visit battleforthenet.com to make sure your lawmakers hear from you about this. It’s almost too late!",

    "███████ ███ ████ ████ ██ ███ ███ ██████████ ██ ████ ███ ████████ ████ ██ ███ █ ██ ██████. Please upgrade your plan to see this tweet: battleforthenet.com",

    "If we lose #NetNeutrality—BLAME CONGRESS. Call your lawmakers now: 202-759-7766 https://www.wired.com/story/fcc-wants-to-kill-net-neutrality-congress-will-pay-the-price/",

    "THIS IS AN INTERNET EMERGENCY: Call Congress now to #StopTheFCC from killing net neutrality and destroying the Internet as we know it: battleforthenet.com",

    "This tweet is being ██████ by your internet provider. Well, not yet. But, that's what will happen if we ████ #StopTheFCC. Congress can stop this. Take action now: battleforthenet.com",

    "You know what's not funny? Screwing over hundreds of millions of people on behalf of a few of the most unpopular companies in the world. #StopTheFCC: battleforthenet.com",

    "Don't let the FCC #breaktheinternet. We can stop this: battleforthenet.com",

    "Don't let your Internet provider [X] this tweet. battleforthenet.com",

    "This tweet is ██████████ by your Internet provider. Stop them: battleforthenet.com",

    "Keep the Internet weird, save #NetNeutrality: battleforthenet.com",

    "Congress has oversight over the FCC and only they can stop them from killing #NetNeutrality. Call them now: battleforthenet.com/call",

    "Without #netneutrality, the Internet will be like cable TV... big companies -- not you -- decide what you see. Take action now: battleforthenet.com",

    "The people who literally invented the Internet are warning the FCC against killing net neutrality: https://pioneersfornetneutrality.tumblr.com/ Join the protest: breaktheinternetprotest.org",

    "Without #netneutrality, indie artists and musicians will struggle to be heard: http://www.rollingstone.com/music/news/net-neutrality-how-a-repeal-could-kill-artists-careers-w513787 Join the protest: https://www.battleforthenet.com/",

    "Millions of Internet users are asking about #NetNeutrality ahead of the FCC’s plan to repeal the rules on December 14th. Head to battleforthenet.com to see what it’s all about and what you can do about it.",

    "Run this twitter-bot to send a message: https://github.com/tuxpowered/twitter-net-neutrality-bot",
]


logger = logging.getLogger("net-neutrality-bot")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(fmt=fmt)
logger.addHandler(ch)



while True:
    random.shuffle(tweets)
    for tweet in tweets:
        try:
            logger.info(tweet)
            api.update_status(tweet)
        except tweepy.TweepError as e:
            logger.critical(e.reason)

        sleep(tweet_delay)

