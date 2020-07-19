import requests
from time import sleep
from bs4 import BeautifulSoup
from csv import writer

# barkha sing search in google and getting all the pics links of it
response = requests.get('https://www.google.com/search?q=barkha+singh&rlz=1C1SQJL_enIN874IN874&sxsrf=ALeKk00dvTB3SiFyGDHENTENN2zQwjxVIw:1595161897893&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj0vqGSqdnqAhXIeisKHbW6BxIQ_AUoAXoECBkQAw&biw=1242&bih=568')

soup = BeautifulSoup(response.text,'html.parser')

# print(soup.body)
posts = soup.find_all('div')
# print(posts[5])

img = posts[5].find_all(class_='t0fcAb')
# print(img)
# print(img[0]['src'])

title = posts[5].find_all(class_='fYyStc')
# print(title)
# # print(len(img),len(title))

# foor writing in the csv file all the results
with open('posts.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['title' , 'link']
    csv_writer.writerow(headers) 

    for i in range(0,len(img)):
        imgp = img[i]['src']
        i = 2*i
        titlep = title[i].get_text()
        csv_writer.writerow([titlep,imgp])






