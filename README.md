# hash notify

特定のハッシュタグがついたツイートを収集し、ソートした後にラインに通知
 
# demo
 
![IMG-3155](https://user-images.githubusercontent.com/117279367/201450295-ea4d16ee-4e14-42c8-bf41-b71e5a9d6a6a.jpg)

 
# Features
何日か分けてつくりましたが、1時間もあればできるのではないでしょうか
「#漫画が読めるハッシュタグ」で検索>人気なものソートにしそのまま自分の個人ラインにURLを生成して投げてます。
SEARCH_KEYWORDの部分を変更するだけで色々なワードを取得できます。

注 :: ベタ書きです！！

CloudFunctionなど利用して定期実行させるといいかもです
https://cloud.google.com/functions?hl=ja

# Requirement
 
* tweepy 
* requests 

 
# Installation
  
```bash
pip install tweepy
```
 
# Usage 
```bash
git clone git@github.com:E-dmp/hash_notify.git
cd examples
python twitter_aggregate.py
```
 
# Note
 
TwitterとLINEのAPIを認証する箇所は返り値がアクセストークンの関数を作成しています。

 
# License
 
"hash notify" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).