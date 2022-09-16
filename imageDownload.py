import requests
import sys

img_url = sys.argv[1] #command line argument. This is the link from we will download image

file_name = sys.argv[2] #In this file we will save the image

r = requests.get(img_url)

with open(file_name, "wb") as f:
    f.write(r.content)