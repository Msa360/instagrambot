
# imports
from pathlib import Path
import os
from dotenv import load_dotenv
from itertools import dropwhile, takewhile
import instaloader
from instaloader import Profile, Post
from datetime import datetime

# set up
load_dotenv()
user_name = os.getenv("USERNAME")
pwd = os.getenv("PASSWORD")

# create an instance
L = instaloader.Instaloader(save_metadata=False, compress_json=False, download_video_thumbnails=False)
# L.login(user_name, pwd)
L.load_session_from_file(user_name)


posts = Profile.from_username(L.context, "new_fork_city").get_posts()

e = 0
for post in takewhile(lambda p: p.date > datetime(2015, 4, 10), dropwhile(lambda p: p.date > datetime(2015, 5, 1), posts)):
    L.download_post(post=post, target=Path('rawscraped/' + post.owner_username))
    e += 1
    print("post downloaded! #" + str(e))








