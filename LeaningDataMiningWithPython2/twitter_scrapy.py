import twitter
import json


comsumer_key = "n1mWjsNz51mTCqH2tLgNFo537"
consumer_secret = "BDYQqKW0pDXAamLjwsa4i80P0wlbXNLyLGY1Gg3Bm4Ps9yqOxN"
access_token = "2427500137-j4mEkKo9ZUXn7LdNOs9Pw5gNMbuXfk47tD7iTAy"
access_secret = "nhEywkPBpuggC2GKz2XB6UHOg4mpa5yoyabNdf7yNd4qv"

auth = twitter.OAuth(access_token,access_secret,comsumer_key,consumer_secret)
t = twitter.Twitter(auth = auth)


with open("file.json","w") as f:
    serach_results = t.search.tweets(q="python",count=100)["statuses"]
    for tweet in tweets:
        if "text" in tweet:
            f.write(json.dumps(tweet["text"]))
            f.write("\n\n")