import tweepy
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
TWEET_COUNT = 500
TWEET_MODE = "extended"
LIKES_COUNTS = 1000
tweet_objects = tweepy.Cursor(api.search_tweets, q=SEARCH_KEYWORD, tweet_mode=TWEET_MODE).items(TWEET_COUNT)



# ツイートソート
sortedResults = {}

def sort_tweet_more_than_thousand(tweet_objects):

    current_max_fav = 0

    """
    1000以上かつ最大のツイートを返却
    return dict
    """
    for tweet in tweet_objects:

        if tweet.favorite_count <= LIKES_COUNTS: 
            continue

        key = tweet.user.screen_name
        
        if key not in sortedResults and tweet.favorite_count >= current_max_fav:

            sortedResults[key] = tweet.id
            current_max_fav = tweet.favorite_count

    return sortedResults

result= sort_tweet_more_than_thousand(tweet_objects)

print(result)



