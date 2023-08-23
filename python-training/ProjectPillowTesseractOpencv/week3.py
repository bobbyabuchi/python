'''
To access the newspapers in the zipfile, you must first use the Zipfile library to open the zipfile then iterate through
the objects (newspapers) in the zipfile using .infolist(). Try and write a simple routine to just go through the zipfile,
printing out the name of the file as well as using display(). Remember that the PIL.Image library can .open() files, and
that items in .infolist() in the zipfile each appear to Python just as if they were a file (these are called "file-like"
objects).
'''

'''
You can spend a lot of time converting between PIL.Image files and byte arrays, but you don't have to. Why not just 
store the PIL.Image objects in a global data structure, maybe a list or a dictionary indexed by name? Then you can 
further process this data structure, by adding in information such as the text detected on the pages or the bounding 
boxes behind faces. Come to think of it, a list of dictionary objects, where each entry in the list would have the PIL 
image, the bounding boxes, and the text discovered on the page, would be a handy way to store this data.
'''

'''
A quick reminder - in Python all strings are just like lists of characters. Kind of (remember they are immutable lists 
- more like tuples!). But this means you can use the in keyword to find substrings really easily. So the following 
statement will return True if the substring is matched: if "Christopher" in my_text
'''

'''
Creating the contact sheet can be a bit of a pain. But you can resize images without having to worry about the aspect 
ratio if you use the PIL.Image.thumbnail function. I used it when creating out the output images, maybe you should too! 
And check out the lecture on the contact sheet, you want to be careful that you don't "walk off" the end of the images 
when creating a row (or column).
'''


import zipfile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!

#-------------------------------------- My Solution -----------------------------------------------------

# define a function to get (name, image, text) from a zip file
def extract_zip(name):

    """
    get all the information (name, image, text) from a zip file

    :input: the name of a zip file
    :output: a list of dictoionaries. Each dictionary contains the all the information
    (name, image, text) of a image object.

    """
    # Assign name to zip_name
    global imageString, i_mage
    my_zip = 'readonly/' + name

    # My Result
    my_result = []

    # index details
    with zipfile.ZipFile(my_zip) as zip_a:
        zip_detail = zip_a.infolist()

    for item in zip_detail:
        name = item.filename
        i_mage = Image.open(zip_a.open(name))
        # get_text - > image to string
        imageString = pytesseract.image_to_string(i_mage.convert('L'))

    # test if "Christopher" or "Mark" are in the text
    if ("Christopher" in imageString) or ("Mark" in imageString):

        # example of dictionary
        dic = {"name":name, "img":i_mage, "text":imageString}
        my_result.append(dic)
    return my_result

# extract all the information related to small_img.zip and images.zip
sm_Images = extract_zip("small_img.zip")
# big_imgs will be here latter
#big_imgs = zip_images_extraction("images.zip")


# big_imgs will be here latter
bg_Images = extract_zip("images.zip")


# define a function to extract a list of faces
# create a contact sheet for these faces
def extract_faces(i_mage, scale_factor):

    # define rectangle of the faces
    gray = np.array(i_mage.convert("L"))
    faces = face_cascade.detectMultiScale(gray, scale_factor)

    # faces not found
    if (len(faces) == 0):
        return None

    # extract faces into the list imgs
    faces_imgs = []

    for x,y,w,h in faces:
        faces_imgs.append(i_mage.crop((x,y,x+w,y+h)))

    # get n rows and n cols
    n_c = 5
    n_r = math.ceil(len(faces) / n_c)

    # contact sheet
    contact_sheet=Image.new(i_mage.mode, (550, 110*n_c))
    x, y = (0, 0)

    for each_face in faces_imgs:
        each_face.thumbnail((110,110))
        contact_sheet.paste(each_face, (x,y))

    if x+110 == contact_sheet.width:
        x = 0
        y += 110
    else:
        x += 110

    return contact_sheet


# search function
def value_search(value, zip_name, scale_factor):

    if my_zip == "small_img.zip":
        ref_imgs = sm_Images
    else:
        ref_imgs = bg_Images

    for item in ref_imgs:
        # check if value  in  text
        if value in item["text"]:
            # print out the name of the figure
            print("Results found in file {}".format(item["name"]))

            # index faces
            i_mage = item["img"]
            contact_sheet = extract_faces(i_mage, scale_factor)
            if contact_sheet is not None:
                display(contact_sheet)
            else:
                print("faces not found")



# reproduce the search for "Christopher"
value = "Christopher"
my_zip = "small_img.zip"
value_search(value, my_zip, scale_factor = 1.4)



# reproduce the search for "Christopher"
value = "Mark"
my_zip = "images.zip"
value_search(value, my_zip, scale_factor = 1.5)


#------------------------------------------------------------

# --- code by Alejandro Guerrero Torres --------------------------------------------

import zipfile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
faces_ = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

zip_data_detail = [
    {
        "file_name": "readonly/small_img.zip",
        "person_name": "Christopher"
    },
    {
        "file_name": "readonly/images.zip",
        "person_name": "Mark"
    }
]


def read_zip_file(file_name):
    images = []

    file = zipfile.ZipFile(file_name)
    for item in file.infolist():
        images.append({"img_object": Image.open(file.open(item.filename)), "file_name": item.filename})

    return images


def get_info(file_name, person_name):
    images = read_zip_file(file_name)

    for i_mage in images:
        i_mage["text"] = pytesseract.image_to_string(i_mage["img_object"])

        if person_name in i_mage["text"]:
            print("Results found in file called {}".format(i_mage["file_name"]))

            try:
                faces_details = (face_cascade.detectMultiScale(np.array(i_mage["img_object"]), 1.35, 4)).tolist()

                i_mage["faces_details"] = faces_details

                faces = []

                for x, y, w, h in i_mage["faces_details"]:
                    faces.append(i_mage["img_object"].crop((x, y, x + w, y + h)))
            except:
                faces = []

            if len(faces) > 0:
                contact_sheet = Image.new(i_mage["img_object"].mode, (550, 110 * int(np.ceil(len(faces) / 5))))

                x = 0
                y = 0
                for face in faces:
                    face.thumbnail((110, 110))

                    contact_sheet.paste(face, (x, y))

                    if x + 110 == contact_sheet.width:
                        x = 0
                        y = y + 110
                    else:
                        x = x + 110

                display(contact_sheet)
            else:
                print('But there were no faces in that file!')


for data_element in zip_data_detail:
    print('RESULTS FOR FILENAME "{}" AND PERSON NAME "{}":\n'.format(data_element["file_name"],
                                                                     data_element["person_name"]))
    get_info(data_element["file_name"], data_element["person_name"])


# -------------------------- code by -------------------------------------------------------------------


