'''
Upload pics
'''
import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
# client_id = 'Your imgur client id'
# client_secret = 'Your imgur client secret'
# album_id = 'Your imgur album id'
# access_token = 'Your imgur access token'
# refresh_token = 'Your imgur refresh token'

# client_id = '2a5690ab2c44302'
# client_secret = 'b98cdf17722e6f2cd17305c6683a6b362b5db5f0'
# # album_id = 'dhCfdAM'
# album_id = 'k-line-ifBQMq1'
# access_token = '59786ca79ba09af3c00a4a7e3ca93cdbf0c15245'
# refresh_token = 'a9a71eaca44f78eb8b5ae37ceea06f0b99f9f47b'

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
