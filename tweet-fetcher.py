import tweepy
import json
import csv

json_auth = json.load(open("twitter-auth.json"))
auth = tweepy.OAuthHandler(json_auth['consumer_key'], json_auth['consumer_secret'])
auth.set_access_token(json_auth['access_token'], json_auth['access_secret'])

api = tweepy.API(auth)
if not (api):
    print("Problem connecting")

with open("bad_words.txt", encoding="utf-8") as bad_words_file:
    bad_words_list = bad_words_file.readlines()
    bad_words_list = [bad_word.strip() for bad_word in bad_words_list]

bad_tweet_file = open('bad_tweets.csv', 'w', encoding="utf-8")

field_names = ['lat', 'lng', 'tweet']
csv_writer = csv.DictWriter(bad_tweet_file, fieldnames=field_names)
csv_writer.writeheader()

for bad_word in bad_words_list:
    list_of_bad_tweets = []
    print(bad_word)
    public_tweets = api.search(q=bad_word, lang="sv", tweet_mode="extended", show_user=True)
    for tweet in public_tweets:
        if tweet.user != "null":
            print(tweet.user)
