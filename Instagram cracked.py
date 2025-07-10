import os
import re
import instaloader
import getpass


login = instaloader.Instaloader()

user = input("User: ")
password = getpass.getpass(prompt="Password: ", stream=None)


try:
    login.login(user=user, passwd=password)
    print(f"Logged in as {user} successfuly")

except Exception as e:
    print(e)

try:
    while True:

        profile = input("Username: ")

        profile = instaloader.Profile.from_username(login.context, profile)
        highs = login.get_highlights(profile)
        stories = login.get_stories(userids=[profile.userid])

        print(f"Total Followers: {profile.followers}")
        print(f"Total Following: {profile.followees}")

        # Download Profile Pic
        login.download_profilepic(profile=profile)

        try:
            # For downloading stories
            if profile.has_public_story:
                print(f"Downloading story...")
                for story in stories:
                    for item in story.get_items():
                        login.download_storyitem(item, target=profile)
                print("Story Downloaded")

        except Exception as e:
            print(f"Story ERROR: {e}")

        try:
            # For downloading highlights
            print("Downloading highlights...")
            login.download_highlights(user=profile)
            print("Highlights downloaded")

        except Exception as e:
            print(f"Highlights ERROR: {e}")

        try:
            # For downloading all posts and comments
            print("Downloading Posts...")
            login.download_profile(profile_name=profile, download_stories=False, profile_pic=False)
            print("Posts downloaded")

            print("Downloading Comments...")
            for posts in profile.get_posts():
                for comments in posts.get_comments():
                    post_time = str(posts.date_utc)
                    post_time = re.sub(r'[<>:"/\\|?*]', "-", post_time)

                    with open(f"{post_time} comments.txt", 'a', encoding="utf-8") as file:  # See all the comments
                        file.write(f"{comments.owner.username} : {comments.text} \n")
            print("Comments Downloaded")

        except Exception as e:
            print(f"Posts and Comments: {e}")
        login.close()

except Exception as e:
    print(e)
