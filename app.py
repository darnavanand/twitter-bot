import tweepy
import time

auth = tweepy.OAuthHandler('tbYGjeRw26qUplazDOihziQ33','nR2Czea8jlICo8zttQOBAKwmbPUixTAlA7McNqo8t9byCmj2Q9')
auth.set_access_token('2998335193-3SQZFEUQbUCfeMmhsuod2hwTrGemii1F4nZkybu', 'AZrHNfMmV56utRPOg1GxTmv5ebSjzCHKpCQATVJXwzXSj')

api = tweepy.API(auth)
while True:
  user= api.get_user('ShraddhaKapoor')
  a=user.followers_count

  api.update_profile(name= f'Arnav Anand {a}')
  print(f'Arnav Anand {a}')
  time.sleep(60)
