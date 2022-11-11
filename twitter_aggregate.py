import tweepy
import requests
from authentication_module import get_authentication_info

#Twitterの認証
api_key = get_authentication_info("api_key")
api_secret = get_authentication_info("api_secret")
access_token = get_authentication_info("access_token")
access_token_secret = get_authentication_info("access_token_secret")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ツイート取得
SEARCH_KEYWORD = "#漫画が読めるハッシュタグ -filter:retweets"
TWEET_COUNT = 1000
TWEET_MODE = "extended"
LIKES_COUNTS = 1000
tweet_objects = tweepy.Cursor(api.search_tweets, q=SEARCH_KEYWORD, tweet_mode=TWEET_MODE).items(TWEET_COUNT)

# ツイートソート

def sort_tweet_more_than_thousand(tweet_objects):

    sortedResults = []
    current_max_fav = 0

    """
    1000以上かつ最大のツイートを返却
    return list
    """
    for tweet in tweet_objects:

        if tweet.favorite_count <= LIKES_COUNTS: 
            continue        
        if tweet.user.screen_name not in sortedResults and tweet.favorite_count > current_max_fav:
            sortedResults = []
            sortedResults.append(tweet.user.screen_name)
            sortedResults.append(tweet.id)
            current_max_fav = tweet.favorite_count

    return sortedResults



result= sort_tweet_more_than_thousand(tweet_objects)
print(result)
user_name,tweet_id = result if result != [] else [None,None]

# LINE の接続
line_notify_token = get_authentication_info("line_notify_token")
line_notify_api = 'https://notify-api.line.me/api/notify'
TWEET_URL = f'https://twitter.com/{user_name}/status/{tweet_id}' if user_name != None else "https://twitter.com/home"

def send_tweet_url_for_line():
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': TWEET_URL}
    requests.post(line_notify_api, headers = headers, data = data)

send_tweet_url_for_line()