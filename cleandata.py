
# functions to clean data and prepare it for usage

import os
from PIL import Image
from cleandataapi import contain_text # function calling an api ocr // False if no text

# used to get captions from scraped medias to use them after for new posts
def get_captions(dir):
    f = open("captions.txt", "a")
    mylist = os.listdir(dir)
    for i in mylist:
        if i[-4:] == ".txt":
            t = open(dir + "/" + i, "r")
            f.write(str(t.read()) + ",\n")
            t.close()
    f.close()

# after getting the captions to a single file, we can delete them in their current file
def delete_captions(dir):
    mylist = os.listdir(dir)
    for i in mylist:
        if i[-4:] == ".txt":
            os.remove(dir + "/" + i)

def convert_webp_to_jpg(dir):
    mylist = os.listdir(dir)
    for i in mylist:
        if i[-5:] == ".webp":
            new_img = Image.open(dir + "/" + i).convert("RGB")
            new_img_name = i[:-5]
            new_img.save(dir + "/" + new_img_name + ".jpg", "jpeg")
            os.remove(dir + "/" + i)

def delete_text_img(dir):
    mylist = os.listdir(dir)
    for i in mylist:
        if i[-4:] == ".jpg" or i[-5:] == ".jpeg":
            if contain_text(dir + "/" + i):
                os.remove(dir + "/" + i)
            


def clean_oneshot(dir: str):

    try:
        get_captions(dir)
    except:
        print('get_captions failed')
    else:
        print('get_captions done successfully')

    try:
        delete_captions(dir)
    except:
        print('delete_captions failed')
    else:
        print('delete_captions done successfully')

    try:
        convert_webp_to_jpg(dir)
    except:
        print('convert_webp_to_jpg failed')
    else:
        print('convert_webp_to_jpg done successfully')

    try:
        delete_text_img(dir)
    except:
        print('delete_text_img failed ')
    else:
        print('delete_text_img done successfully')

    print("cleaning finished")

# clean_oneshot('./rawscraped/test')


    







