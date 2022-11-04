import tweepy
from authentication_module import get_authentication_info

#Twitterの認証
api_key = get_authentication_info("api_key")
api_secret = get_authentication_info("api_secret")
access_key = get_authentication_info("access_key")
access_secret = get_authentication_info("access_secret")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

