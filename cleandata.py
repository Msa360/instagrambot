
# functions to clean data and prepare it for usage

import os


# used to get captions from scraped medias to use them after for new posts
def get_captions(dir):
    f = open("captions.txt", "a")
    mylist = os.listdir(dir)
    for i in mylist:
        if i[-4:] == ".txt":
            t = open(dir + "/" + i, "r")
            f.write(str(t.read()) + ", ")
            t.close()
    f.close()

# after getting the captions to a single file, we can delete them in their current file
def delete_captions(dir):
    mylist = os.listdir(dir)
    for i in mylist:
        if i[-4:] == ".txt":
            os.remove(dir + "/" + i)






