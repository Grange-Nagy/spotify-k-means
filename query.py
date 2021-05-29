from time import sleep
import cv2
from sklearn.cluster import KMeans
import numpy as np
from skimage import io
import spotipy
import spotipy.util as util
import imutils
import os


def dominantColors(url,clusters=3):

    #read image
    img = imutils.url_to_image(url)
    cv2.imshow('Currently Playing', img)
    
    #convert to lab from bgr
    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            
    #reshaping to a list of pixels
    img = img.reshape((img.shape[0] * img.shape[1], 3))
    
    
    #using k-means to cluster pixels
    kmeans = KMeans(n_clusters=clusters)
    kmeans.fit(img)
    
    colors = kmeans.cluster_centers_
    colors = cv2.cvtColor(np.uint8([colors]), cv2.COLOR_LAB2RGB)
    colors = colors[0]

    #returning after converting to integer from float
    return colors.astype(int)


secretFile = open('secret.txt')

os.environ['SPOTIPY_CLIENT_ID'] = secretFile.readline().strip()
os.environ['SPOTIPY_CLIENT_SECRET'] = secretFile.readline().strip()
os.environ['SPOTIPY_REDIRECT_URI'] = secretFile.readline().strip()

token = util.prompt_for_user_token(secretFile.readline().strip(), 'user-read-currently-playing')
secretFile.close()

lastURL = ""

while(True):
    

    track = spotipy.Spotify(token).current_user_playing_track()
    imageURL = track['item']['album']['images'][0]['url']

    if(lastURL != imageURL):
        lastURL = imageURL
        colors = dominantColors(imageURL,4)

        palette = np.array(colors, dtype=np.uint8)
        display = np.array([[0,1],[2,3]], dtype=np.uint8)

        io.imshow(palette[display])
        io.show()

        
    sleep(1)
