
# imports
import os
import random
from dotenv import load_dotenv



# set up
# load_dotenv()
# user_name = os.getenv("USERNAME")
# pwd = os.getenv("PASSWORD")


def post():
    account = random.choice(os.listdir('rawscraped'))
    file = random.choice(os.listdir('rawscraped/' + account))
    file_path = "rawscraped/" + account + "/" + file
    os.replace(file_path, "new_place") # to be continued


    

