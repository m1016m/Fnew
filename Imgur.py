import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
# client_id = 'Your imgur client id'
# client_secret = 'Your imgur client secret'
# album_id = 'Your imgur album id'
# access_token = 'Your imgur access token'
# refresh_token = 'Your imgur refresh token'

# ALBUM_ID zV0K1Ch


# Client ID:
# 882cbc78178ab1b
# Client secret:
# 3eb5a0d648a492944f1748b4a9614a3a59bbe7c1

# https://imgur.com/#access_token=96101a97afcea12b51b4c9c7a42f9e961bc38513&expires_in=315360000&token_type=bearer&
# refresh_token=efdc4440c8cc008113a964a6629db78825306084&account_username=m1016m&account_id=112443063

client_id = '882cbc78178ab1b'
client_secret = '3eb5a0d648a492944f1748b4a9614a3a59bbe7c1'
album_id = 'zV0K1Ch'
access_token = '96101a97afcea12b51b4c9c7a42f9e961bc38513'
refresh_token = 'efdc4440c8cc008113a964a6629db78825306084'


def showImgur(fileName):
        # connect imgur
        client= ImgurClient(client_id, client_secret, access_token, refresh_token)
    
        # params
        config = {
            'album': album_id, # album name
            'name': fileName, # pics name
            'title': fileName, # pics title
            'description': str(datetime.date.today())
            }
        
        # Upload file
        try:
            print("[log:INFO]Uploading image... ")
            imgurl = client.upload_from_path(fileName+'.png', config=config, anon=False)['link']
            #string to dict
            print("[log:INFO]Done upload. ")
        except :
            # if faild to upload
            imgurl = 'https://i.imgur.com/RFmkvQX.jpg'
            print("[log:ERROR]Unable upload ! ")
            
        
        return imgurl