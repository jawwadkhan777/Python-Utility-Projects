# webscrapping code:

from urllib import request
file_url = 'j:\\python\\webscrapping.txt'
file = open(file_url, 'wb')
website_url = request.urlopen('http://olympus.realpython.org/profiles/poseidon')
read_in_bytes = website_url.read()
file.write(read_in_bytes)
file.close()

file = open(file_url, 'r')
x = file.read()
##print(x)

image_scrapping = x.find("<img")
while (image_scrapping != -1):
    starting_image = x.find('"' , image_scrapping)
    ending_image = x.find('"' , starting_image+1)
    print('images on this website is/are:' , x[starting_image+1 : ending_image])
    image_scrapping = x.find("<img" , ending_image+1)

