# Imports requests library for handling HTTP requests.
import requests

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
        print("Post id:"+post_ids[pos],"\n Post link:"+ post_links[pos])
    elif int(choice) == 2:
        max_comments = max(post_comments)
        pos = post_comments.index(max_comments)
        print( "Post id:"+post_ids[pos],"\n Post link:" +post_links[pos])


#interaction with instabot
print("\nHello!!! Welcome to the Instabot.")
choice = '1'
while choice != '3':
    print("\nWhat do you want to do using the bot?")
    print("1. Get the Details of the owner.")
    print("2. Get the most popular media.")
    print("3. Exit.\n\n")

    choice = input("Enter Your Choice(1-3) : ")

# Perform Actions Depending on the User's Choice. Runs Until User wishes to Exit.
    if choice in ['1', '2', '3']:
        if int(choice)==1:
           owner_info()

        if int(choice)==2:
           most_popular()

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
    elif choice == '3':
        pass
    else:
        print("\nWrong choice entered.... Try Again.")

# Terminates the Program by Printing a Message.
print(" Thanks for using Instabot. ")
