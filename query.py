from time import sleep
import cv2
from sklearn.cluster import KMeans
import numpy as np
from skimage import io
import spotipy
from spotipy import oauth2
import spotipy.util as util
import imutils
import os

#use k-means in lab colorspace to determine dominant colors
def dominantColors(url,clusters):

    #read image
    img = imutils.url_to_image(url)
    #cv2.imshow('Currently Playing', img)
    
    #convert to lab from bgr
    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            
    #reshaping to a list of pixels
    img = img.reshape((img.shape[0] * img.shape[1], 3))
    
    
    #using k-means to cluster pixels
    kmeans = KMeans(n_clusters=clusters)
    kmeans.fit(img)
    
    colors = kmeans.cluster_centers_

    #convert to 3d for conversion then back to 2d
    colors = cv2.cvtColor(np.uint8([colors]), cv2.COLOR_LAB2RGB)[0]

    return colors.astype(int)


secretFile = open('secret.txt')

os.environ['SPOTIPY_CLIENT_ID'] = secretFile.readline().strip()
os.environ['SPOTIPY_CLIENT_SECRET'] = secretFile.readline().strip()
os.environ['SPOTIPY_REDIRECT_URI'] = secretFile.readline().strip()

userID = secretFile.readline().strip()
secretFile.close()


spotify = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope='user-read-currently-playing',cache_path='.cache-'+userID))


lastURL = ""

while(True):

    #token should refresh automatically
    track = spotify.current_user_playing_track()

    #check if track is None
    if(track != None):
        imageURL = track['item']['album']['images'][0]['url']

    #if the song has changed
    if(lastURL != imageURL):
        lastURL = imageURL
        colors = dominantColors(imageURL,4)

        palette = np.array(colors, dtype=np.uint8)
        display = np.array([[0,1],[2,3]], dtype=np.uint8)

        print(colors)
        #io.imshow(palette[display])
        #io.show()

    sleep(1)
