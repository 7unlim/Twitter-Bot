import tweepy
import keys
import time
import random
from list import list

while True:

    def api():
        auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)

        return tweepy.API(auth)


    random.shuffle(list)
    for message in list: 
        def tweet(api: tweepy.API, message:str, image_path=None):
            if image_path:
                api.update_status_with_media(message, image_path) 
            else: 
                api.update_status(message)

            print("Confirmation")

    if __name__ =='__main__':
            api=api()
            tweet(api, message + " " + "is a work of art.") #to add image simply add parameter here
            time.sleep(10)
