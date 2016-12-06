# Twython Test

from twython import Twython

# Twitter App Keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# zimchaa User Keys
ACCESS_KEY = ''
ACCESS_SECRET = ''

# create the client
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# tweet something!
TWEET = 'Trying again without using the deprecated update_status_with_media call - which seemed nice #sadface #twython'
PHOTO = open('simple_shot_2016-12-03-18-55-47.jpg', 'rb')
print('Tweeting this:')
print(TWEET)

# Uploading media to avoid the deprecated update_status_with_media call, which seemed nice... #sadface
print('Uploading picture...')
media_response = twitter.upload_media(media=PHOTO)
print('Media IDs:')
print(media_response['media_id'])

twitter.update_status(status=TWEET, media_ids=[media_response['media_id']])

print('Success!')
