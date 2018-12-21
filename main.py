# Imports requests library for handling HTTP requests.
import requests
# Library to print Python data structures in a well-formatted and more readable way!
import pprint

# Access Token generated from Instabot servers.
APP_ACCESS_TOKEN = '6006342728.5cb0e0a.dae74d1e0dd84262b176c2dcf8ded0dc'

# Base URL for every URL used in the file.
BASE_URL = 'https://api.instagram.com/v1/'

# Function to print details of the owner.
def print_owner_info(data):
    print("Name                    : ", data['data']['full_name'])
    print("Username                : ", data['data']['username'])
    print("Link to Profile Picture : ", data['data']['profile_picture'])
    print("Media Shared            : ", data['data']['counts']['media'])
    print("Followed By             : ", data['data']['counts']['followed_by'])
    print("Followers               : ", data['data']['counts']['follows'])
    if data['data']['website'] != '':
        print("Website                 : ", data['data']['website'])
    else:
        print("Website                 :  No Website Available")
    if data['data']['bio'] != '':
        print("Bio                     : ", data['data']['bio'])
    else:
        print("Bio                     :  No Info Available")

# function to get the details of owner.
def owner_info():
    url = BASE_URL + 'users/self/?access_token=' + APP_ACCESS_TOKEN
    data = requests.get(url).json()
    print_owner_info(data)

#function to get the details of media of the owner.
def media_info():
    url = BASE_URL + 'users/self/media/recent/?access_token=' + APP_ACCESS_TOKEN
    data = requests.get(url).json()
    print(data)

#function to get the most popular media of the owner.
def most_popular():
    url = BASE_URL + 'users/self/media/recent/?access_token=' + APP_ACCESS_TOKEN
    data = requests.get(url).json()
    post_ids = []
    post_likes = []
    post_comments = []
    post_links = []
    for media in (data['data']):
        post_ids.append(media['id'])
        post_likes.append(media['likes']['count'])
        post_comments.append(media['comments']['count'])
        post_links.append(media['link'])
    print("\nWhich Recent Post you wanna select ?")
    print("1. The one with maximum likes.")
    print("2. The one with maximum comments.")
    choice = input("\nEnter your choice (1 or 2) : ")
    if choice not in ['1', '2']:
        while choice not in ['1', '2']:
            print("You entered the wrong choice. Please choose from given options.")
            choice = input("Enter your choice (1 or 2) : ")
    if int(choice) == 1:
        max_likes = max(post_likes)
        pos = post_likes.index(max_likes)
        return post_ids[pos],post_links[pos]
    elif int(choice) == 2:
        max_comments = max(post_comments)
        pos = post_comments.index(max_comments)
        return post_ids[pos], post_links[pos]

#function to get the least popular media of the owner.
def least_popular():
    url = BASE_URL + 'users/self/media/recent/?access_token=' + APP_ACCESS_TOKEN
    data = requests.get(url).json()
    post_ids = []
    post_likes = []
    post_comments = []
    post_links = []
    for media in (data['data']):
        post_ids.append(media['id'])
        post_likes.append(media['likes']['count'])
        post_comments.append(media['comments']['count'])
        post_links.append(media['link'])
    print("\nWhich Recent Post you wanna select ?")
    print("1. The one with minimum likes.")
    print("2. The one with minimum comments.")
    choice = input("\nEnter your choice (1 or 2) : ")
    if choice not in ['1', '2']:
        while choice not in ['1', '2']:
            print("You entered the wrong choice. Please choose from given options.")
            choice = input("Enter your choice (1 or 2) : ")
    if int(choice) == 1:
        min_likes = min(post_likes)
        pos = post_likes.index(min_likes)
        return post_ids[pos], post_links[pos]
    elif int(choice) == 2:
        min_comments = min(post_comments)
        pos = post_comments.index(min_comments)
        return post_ids[pos], post_links[pos]

# Function to get the comments.
def media_comments():
    print("\nWhich post's comments you wanna select ?")
    print("1. The most popular one.")
    print("2. The least popular one.")
    choice = input("\nEnter your choice (1 or 2) : ")
    if choice not in ['1', '2']:
        while choice not in ['1', '2']:
            print("You entered the wrong choice. Please choose from given options.")
            choice = input("Enter your choice (1 or 2) : ")
    if int(choice) == 1:
        post_ids,post_links = most_popular()

    elif int(choice)==2:
        post_ids, post_links = least_popular()

    url = BASE_URL + 'media/' + post_ids + '/comments?access_token=' + APP_ACCESS_TOKEN
    data = requests.get(url).json()
    for i in data["data"]:
        print(i["text"])

#interaction with instabot
print("\nHello!!! Welcome to the Instabot.")
choice = '1'
while choice != '6':
    print("\nWhat do you want to do using the bot?")
    print("1. Get the Details of the owner.")
    print("2. Get the Details of media of owner.")
    print("3. Get the most popular media.")
    print("4. Get the least popular media.")
    print("5. Get the comments of media.")
    print("6. Exit.\n\n")

    choice = input("Enter Your Choice(1-6) : ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        if int(choice)==1:
           owner_info()

        if int(choice)==2:
           media_info()

        if int(choice)==3:
           post_id,post_link = most_popular()
           print("\nPost id:",post_id)
           print("\nPost link:", post_link)

        if int(choice)==4:
           post_id, post_link = least_popular()
           print("\nPost id:", post_id)
           print("\nPost link:", post_link)

        if int(choice)==5:
           media_comments()

        print("\nWant to do more using Instabot?")
        ch = 'P'
        flag = 0
        while ch not in ['Y', 'N']:
            if flag != 0:
                print("Wrong Choice Entered. Try Again...")
            ch = input("\nEnter your choice (Y/N) :").upper()
            flag = 1
            if ch == 'N':
                break
    if ch == 'N':
        break;
    elif choice == '6':
        pass
    else:
        print("\nWrong choice entered.... Try Again.")

# Terminates the Program by Printing a Message.
print(" Thanks for using Instabot. ")
