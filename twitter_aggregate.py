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
SEARCH_KEYWORD = "#漫画がよめるハッシュタグ -filter:retweets"
tweet_objects = api.search_tweets(q=SEARCH_KEYWORD,result_type="recent",count=100)

# ツイートソート
LIKES_COUNTS = 500

tweetids_with_more_than_thousand_likes = []
accounts_with_more_than_thousand_likes = []


def sortTweet(tweet_objects):
    """
    リツイート,メンションを除く
    1000以上のいいねがついたuser,idを返却
    """
    for tweet in tweet_objects:

        if tweet.favorite_count <= LIKES_COUNTS:
            continue

        tweetids_with_more_than_thousand_likes.append(tweet.id)
        accounts_with_more_than_thousand_likes.append(tweet.user.screen_name)

    return [accounts_with_more_than_thousand_likes,tweetids_with_more_than_thousand_likes]

accounts,tweetids= sortTweet(tweet_objects)

print(accounts)
print(tweetids)



