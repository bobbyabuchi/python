# Project with Pillow, Tesseract and OpenCV Libraries/Modules Week 1 -------------------------------------------

# Welcome to Python Project: PILLOW, tesseract, and opencv

'''
-> download git-bash
-> download anaconda (for juyter notebook)
Open the git-bash/command-prompt as an admin and Use:
> pip install pillow
> pip install pytesseract
> pip install numpy
> pip install matplotlib
> pip install opencv-python
to install these packages
'''

# The Python Imaging Library (PIL)
'''
The Python Imaging Library, which is known as PIL or PILLOW, is the main library we use in python for dealing with image
 files. This library is not included with python - it's what's known as a third party library, which means you have to 
 download and install it yourself. In the Coursera system, this has all been done for you. 
 Lets do a little exploring of pillow in the jupyter notebooks.
'''
# import the library using the `import` keyword.
import PIL

# check their version using the version attribute. PIL.__version__

# To open an image with `Pillow`. Python provides some built-in functions to help us
# For instance, the help function, when called on any object, returns the object’s built-in documentation.
help(PIL)

# This shows us that there are a host of classes available to us in the module, as well as version information
# and even the file, called __init__.py, which has the source code for the module itself. We could look up
# the source code for this in the Jupyter console if we wanted to. These documentation standards make it easy
# to poke around an unexplored library.
#
# Python also has a function called dir() which will list the contents of an object. This is especially useful
# with modules where you might want to see what classes you might interact with. Lets list the details of
# the PIL module
dir(PIL)

# At the top of the list, there is something called Image. This sounds like it could be interesting, so lets
# import it directly, and run the help command on it.
from PIL import Image
help(Image)

'''
Running help() on Image tells us that this object is "the Image class wrapper". We see from the top level documentation 
about the image object that there is "hardly ever any reason to call the Image constructor directly", and they suggest 
that the open function might be the way to go.
'''

# Lets call help on the open function to see what it's all about. Remember that since we want to pass in the
# function reference, and not run the function itself, we don't put paretheses behind the function name.
help(Image.open)

# It looks like Image.open() is a function that loads an image from a file and returns an instance
# of the Image class. Lets give it a try. In the read_only directory there is an image I've provided
# which is from our Master's of Information program recruitment flyer. Lets try and load that now

file="readonly/msi_recruitment.gif"
image=Image.open(file)
print(image)

'''
------- Output --------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-eb066c68ec5d> in <module>
      4 
      5 file="readonly/msi_recruitment.gif"
----> 6 image=Image.open(file)
      7 print(image)

NameError: name 'Image' is not defined
'''

# Ok, we see that this returns us a kind of PIL.GifImagePlugin.GifImageFile. At first this might
# seem a bit confusing, since because we were told by the docs that we should be expecting a
# PIL.Image.Image object back. But this is just object inheritance working! In fact, the object
# returned is both an Image and a GifImageFile. We can use the python inspect module to see this
# as the getmro function will return a list of all of the classes that are being inherited by a
# given object. Lets try it.

import inspect
print("The type of the image is " + str(type(image)))
inspect.getmro(type(image))

'''
------ output ---------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-940636781f88> in <module>
      7 
      8 import inspect
----> 9 print("The type of the image is " + str(type(image)))
     10 inspect.getmro(type(image))

NameError: name 'image' is not defined
'''

# Now that we are comfortable with the object. How do we view the image? It turns out that the
# image object has a show function. You can find this by looking at all of the properties of
# the object if you wanted to, using the dir() function.
image.show()

'''
---------- Output -----------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-b15abcd2d0f7> in <module>
      2 # image object has a show function. You can find this by looking at all of the properties of
      3 # the object if you wanted to, using the dir() function.
----> 4 image.show()

NameError: name 'image' is not defined
'''

# Common Functions in the Python Imaging Library
# Lets take a look at some of the common tasks we can do in python using the pillow library.

import PIL
from PIL import Image
# And lets import the display functionality
from IPython.display import display
# And finally, lets load the image we were working with last time
file="readonly/msi_recruitment.gif"
image=Image.open(file)

# Great, now lets check out a few more methods of the image library. First, we'll look at copy
# And if you remember, we can do this using the built in python help() function
help(image.copy)

# The save method has a couple of parameters which are interesting. The first, called fp, is the filename
# we want to save the object too. The second, format, is interesting, it allows us to change the type of
# the image, but the docs tell us that this should be done automatically by looking at the file extension
# as well. Lets give it a try -- this file was originally a GifImageFile, but I bet if we save it with a
# .png format and read it in again we'll get a different kind of file
image.save("msi_recruitment.png")
image=Image.open("msi_recruitment.png")
import inspect
inspect.getmro(type(image))

# Indeed, this created a new file, which we could view by going to the Jupyter notebook file list by clicking
# on the logo at the top of the browser, and we can see this new object is actually a PngImageFile object
# For the purposes of this class the difference in image formats isn't so important, but it's nice that you can
# explore how a library works using the functions of help(), dir() and getmro().
#
# The PILLOW library also has some nice image filters to add some effects. It does this through the filter()
# function. The filter() function takes a Filter object, and those are all stored in the ImageFilter object.
# Lets take a look.
from PIL import ImageFilter
help(ImageFilter)

# There are a bunch of different filters here, but lets just try and apply the BLUR filter. Before we do this
# we have to convert the image to RGB mode. This is a bit magical -- images like gifs are limited in how many
# colors can be displayed at once based on the size of the pallet. This is similar to a painters pallet, which
# only has so much room. This is actually a very old image file format. If we convert the image into something
# more sophisticated we can apply these interesting image transforms. Sometimes learning a new library means
# digging a bit deeper into the domain the library is about. We can convert the image using the convert()
# function.
image=image.convert('RGB') # this stands for red, green blue mode
blurred_image=image.filter(PIL.ImageFilter.BLUR)
display(blurred_image)

# Ok, let me show you one more function in the lecture, which is crop(). This removes portions of the image
# except for the bounding box you describe. When you think of images, think of individual dots or pixels
# which make up that image being lined up in a grid. You can actually see the number of pixels high the image
# is and the width of the image
print("{}x{}".format(image.width, image.height))

# This means that the image is 800 pixels wide (the X axis), and 450 pixels high (the Y axis). If we take a
# look at the crop documentation we see that the first parameter to the function is a tuple which is the
# left, upper, right, and lower values of the X/Y coordinates
help(image.crop)

# With PIL images, we define the bounding box using the upper left corner and the lower right corner. And
# we count the number of pixels out from the upper left corner, which is 0,0. This might seem odd if you're
# used to coordinate systems where you start in the lower left -- just remember that we define our box in the
# same way we count out positions in the image.
#
# So, if we wanted to get the Michigan logo out of this image, we might start with the left at, say 50 pixels,
# and the top at 0 pixels, then we might walk to the right another 190 pixels, and set the lower bound to say
# 150 pixels
display(image.crop((50,0,190,150)))

# Of course crop(), like other functions, only returns a copy of the image, and doesn't change the image itself.
# A strategy I like to do is try and draw the bounding box directly on the image, when I'm trying to line things
# up. We can draw on images using the ImageDraw object. I'm not going to go into this in detail, but here's a
# quick example of how. I might draw the bounding box in this case.
from PIL import ImageDraw
drawing_object=ImageDraw.Draw(image)
drawing_object.rectangle((50,0,190,150), fill = None, outline ='red')
display(image)

'''
Ok, that's been an overview of how to use PIL for single images. But, a lot of work might involve multiple images, and 
putting images together. In the next lecture we'll tackle that, and set you up for the assignment.
'''

# Additional PILLOW functions
# Lets take a look at some other functions we might want to use in PILLOW to modify images.

# First, lets import all of the library functions we need
import PIL
from PIL import Image
from IPython.display import display

# And lets load the image we were working, and we can just convert it to RGB inline
file="readonly/msi_recruitment.gif"
image=Image.open(file).convert('RGB')

display(image)

# First, lets import all of the library functions we need
import PIL
from PIL import Image
from IPython.display import display

# And lets load the image we were working, and we can just convert it to RGB inline
file="readonly/msi_recruitment.gif"
image=Image.open(file).convert('RGB')

display(image)

# A task that is fairly common in image and picture manipulation is to create contact sheets of images.
# A contact sheet is one image that actually contains several other different images. Lets try and make
# a contact sheet for the Master of Science in Information advertisment image. In particular, lets change
# the brightness of the image in ten different ways, then scale the image down smaller, and put them side
# by side so we can get the sense of which brightness we might want to use.
#
# First up, lets import the ImageEnhance module, which has a nice object called Brightness
from PIL import ImageEnhance
# Checking the online documentation for this function, it takes a value between 0.0 (a completely black
# image) and 1.0 (the original image) to adjust the brightness. All of the classes in the ImageEnhance module
# do this the same way, you create an object, in this case Brightness, then you call the enhance function()
# on that object with an appropriate parameter.
#
# Lets write a little loop to generate ten images of different brightness. First we need the Brightness
# object with our image
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(0, 10):
    # We'll divide i by ten to get the decimal value we want, and append it to the images list
    # we actually call the brightness routine by calling the enhance() function. Remember, you can dig into
    # details of this using the help() function, or by consulting web docs
    images.append(enhancer.enhance(i/10))
# We can see the result here is a list of ten PIL.Image.Image objects. Jupyter nicely prints out the value
# of python objects nested in lists
print(images)

# Lets take these images now and composite them, one above another, in a contact sheet.
# There are several different approaches we can use, but I'll simply create a new image which is like
# the first image, but ten times as high. Lets check out the PIL.Image.new functionality
help(PIL.Image.new)

# The new function requires that we pass it a mode. We're going to use the mode 'RGB' which stands for
# Red, Green, and Blue, and is the mode of our current first image. There are lots of different image mode
# formats, and this one is most common.
# For the size we have a tuple, which is the width of the image and the height. We'll use the width of our
# current first image, but for the height we'll multiple this by ten. This will make a sort of "canvas" for
# our contact sheet. Finally, the color is optional, and we'll just leave it at black.
first_image=images[0]
from PIL import Image
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width,10*first_image.height))

# So now we have a black image that's ten times the size of the other images in the contact_sheet
# variable. Now lets just loop through the image list and paste() the results in. The paste() function
# will be called on the contact_sheet object, and takes in a new image to paste, as well as an (x,y)
# offset for that image. In our case, the x position is always 0, but the y location will change by
# 450 pixels each time we iterate through the loop.
#
# Lets first create a counter variable for the y location. It will start at zero
current_location = 0
for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (0, current_location) )
    # And update the current_location counter
    current_location=current_location+450

# This contact sheet has gotten big: 4,500 pixels tall! Lets just resize this sheet for display. We can do
# this using the resize() function. This function just takes a tuple of width and height, and we'll resize
# everything down to the size of just two individual images
contact_sheet = contact_sheet.resize((160,900) )
# Now lets just display that composite image
display(contact_sheet)

# Ok, that's a nice proof of concept. But it's a little tough to see. Lets instead change this to a three
# by three grid of values. First thing we should do is make our canvas, and we'll make it 3 times the
# width of our image and 3 times the height of our image - a nine image square
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
# Now we want to iterate over our images and place them into this grid. Remember that in PIL we manage the
# location of where we refer to as an image in the upper right hand corner, so this will be 0,0. Lets use
# one variable for the X dimension, and one for the Y dimension.
x=0
y=0

# Now, lets iterate over our images. Except, we don't want to both with the first one, because it is
# just solid black. Instead we want to just deal with the images after the first one, and that should
# give us nine in total
for img in images[1:]:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# Now lets resize the contact sheet. We'll just make it half the size by dividing it by two. And, because
# the resize function needs to take round numbers, we need to convert our divisions from floating point
# numbers into integers using the int() function.
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
# Now lets display that composite image
display(contact_sheet)

'''
Well, that's been a tour of our first external API, the Python Imaging Library, or pillow module. In this series of 
lectures you've learned how to read and write images, manipulat them with pillow, and explore the functionality of 
third party APIs using features of Python like dir(), help(), and getmro(). You've also been introduced to the console, 
and how python stores these libraries on the computer. While for this course all of the libraries are included for you 
in the Coursera system, and you won't need to install your own, it's good to get a the idea of how this work in case 
you wanted to set this up on your own.

Finally, while you can explore PILLOW from within python, most good modules also put their documentation up online, 
and you can read more about PILLOW here: https://pillow.readthedocs.io/en/latest/
'''

# Project with Pillow, Tesseract and OpenCV Libraries/Modules Week 2 -------------------------------------------

# Lecture: The (Py)Tesseract Library
#--------------------------------------------------------------------------------------------------------

# We're going to start experimenting with tesseract using just a simple image of nice clean text.
# Lets first import Image from PIL and display the image text.png.
from PIL import Image

image = Image.open("readonly/text.png")
display(image)

# Great, we have a base image of some big clear text
# Lets import pytesseract and use the dir() fundtion to get a sense of what might be some interesting
# functions to play with
import pytesseract
dir(pytesseract)

# It looks like there are just a handful of interesting functions, and I think image_to_string
# is probably our best bet. Lets use the help() function to interrogate this a bit more
help(pytesseract.image_to_string)

# So this function takes an image as the first parameter, then there are a bunch of optional parameters,
# and it will return the results of the OCR. I think it's worth comparing this documentation string
# with the documentation we were receiving from the PILLOW module. Lets run the help command on the
# Image resize function()
help(Image.Image.resize)

# Notice how the PILLOW function has a bit more information in it. First it's using a specific format
# called reStructuredText, which is similar in intent to document markups such as HTML, the language of
# the web. The intent is to embed semantics in the documentation itself. For instance, in the resize()
# function we see the words "param size" with colons surrounding it. This allows documentation engines
# which create web docs from source code to link the parameter to the extended docs about that parameter.
# In this case the extended docs tell us that the size should be passed as a tuple of width and height.
# Notice how the docs for image_to_string, for instance, indicate that there is a "lang" parameter we can
# use, but then fail to say anything about what that parameter is for or what its format is.
#
# What this really means is that we need to dig deeper. Here's a quick hack if you want to look at the
# source code of a function -- you can use the inspect getsource() command and print the results
import inspect
src = inspect.getsource(pytesseract.image_to_string)
print(src)

# There's actually another way in jupyter, and that's to append *two* question marks to the end of
# a given function or module. Other editors have similar features, and is a great reason to use a
# software development environment
pytesseract.image_to_string??

# We can see from the source code that there really isn't much more information about what the parameters
# are for this image_to_string function. This is because underneath the pytesseract library is calling a C++
# library which does all of the hard work, and the author just passes through all of the calls to the
# underlying tesseract executable. This is a common issue when working with python libraries, and it means
# we need to do some web sleuthing in order to understand how we can interact with tesseract.
#
# In a case like this I just googled "tesseract command line parameters" and the first hit was what I was
# looking for, here's the URL: https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage
#
# This goes to a wiki page which describes how to call the tesseract executable, and as we read down we see
# that we can actually have tesseract use multiple languages in its detection, such as English and Hindi, by
# passing them in as "eng+hin". Very cool.


# One last thing to mention - the image_to_string() function takes in an "image", but the docs don't
# really describe what this image is underneath. Is it a string to an image file? A PILLOW image?
# Something else?
#
# Again we have to sleuth (and/or experiment) to understand what we should do. If we look at the source
# code for the pytesseract library, we see that there is a function called run_and_get_output(). Here's
# a link to that function on the author's github account:
# https://github.com/madmaze/pytesseract/blob/d1596f7f59a517ad814b7d810ccdef7d33763221/src/pytesseract.py#L199
#
# In this function we see that one of the first things which happens is the image is saved through
# the save_image() function. Here's that line of code:
# https://github.com/madmaze/pytesseract/blob/d1596f7f59a517ad814b7d810ccdef7d33763221/src/pytesseract.py#L116
#
# And we see there that another function is called, prepare(image), which actually loads the image as a
# PILLOW image file. So yes, sending a PIL image file is appropriate use for this function! It sure would
# have been useful for the author to have included this information in reStructuredText to help us not have
# to dig through the implementation. But, this is an open source project -- maybe you would like to contribute
# back better documentation?
#
# Hint: The doc line we needed was :param image: A PIL Image.Image file or an ndarray of bytes
#
# In the end, we often don't do this full level of investigation, and we just experiment and try things. It
# seems likely that a PIL Image.Image would work, given how well known PIL is in the python world. But still,
# as you explore and use different libraries you'll see a breadth of different documentation norms, so it's
# useful to know how to explore the source code. And now that you're at the end of this course, you've got
# the skills to do so!
#
# Ok, lets try and run tesseract on this image
text = pytesseract.image_to_string(image)
print(text)

# Looks great! We see that the output includes new line characters, and faithfully represents the text
# but doesn't include any special formatting. Lets go on and look at something with a bit more nuance to it.

# More Tesseract
# -----------------------------------------------------------------------------------------------------------

# In the previous example, we were using a clear, unambiguous image for conversion. Sometimes there will
# be noise in images you want to OCR, making it difficult to extract the text. Luckily, there are
# techniques we can use to increase the efficacy of OCR with pytesseract and Pillow.
#
# Let's use a different image this time, with the same text as before but with added noise in the picture.
# We can view this image using the following code.
from PIL import Image
img = Image.open("readonly/Noisy_OCR.PNG")
display(img)

# As you can see, this image had shapes of different opacities behind the text, which can confuse
# the tesseract engine. Let's see if OCR will work on this noisy image
import pytesseract
text = pytesseract.image_to_string(Image.open("readonly/Noisy_OCR.PNG"))
print(text)

# This is a bit surprising given how nicely tesseract worked previously! Let's experiment on the image
# using techniqes that will allow for more effective image analysis. First up, lets change the size of
# the image

# First we will import PIL
import PIL
# Then set the base width of our image
basewidth = 600
# Now lets open it
img = Image.open("readonly/Noisy_OCR.PNG")
# We want to get the correct aspect ratio, so we can do this by taking the base width and dividing
# it by the actual width of the image
wpercent = (basewidth / float(img.size[0]))
# With that ratio we can just get the appropriate height of the image.
hsize = int((float(img.size[1]) * float(wpercent)))
# Finally, lets resize the image. antialiasing is a specific way of resizing lines to try and make them
# appear smooth
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
# Now lets save this to a file
img.save('resized_nois.png') # save the image as a jpg
# And finally, lets display it
display(img)
# and run OCR
text = pytesseract.image_to_string(Image.open('resized_nois.png'))
print(text)

# hrm, no improvement for resizing the image. Let's convert the image to greyscale. Converting images
# can be done in many different ways. If we poke around in the PILLOW documentation we find that one of
# the easiest ways to do this is to use the convert() function and pass in the string 'L'
img = Image.open('readonly/Noisy_OCR.PNG')
img = img.convert('L')
# Now lets save that image
img.save('greyscale_noise.jpg')
# And run OCR on the greyscale image
text = pytesseract.image_to_string(Image.open('greyscale_noise.jpg'))
print(text)

# Wow, that worked really well! If we look at the help documentation using the help function
# as in help(img.convert) we see that the conversion mechanism is the ITU-R 601-2 luma transform.
# There's more information about this out there, but this method essentially takes a three channel image,
# where there is information for the amount of red, green, and blue (R, G, and B), and reduces it
# to a single channel to represent luminosity. This method actually comes from how standard
# definition television sets encoded color onto black and while images. If you get really interested
# in image manipulation and recognition, learning about color spaces and how we represent color, both
# computationally and through human perception, is really an interesting field.

# Even though we have now the complete text of the image, there are a few other techniques
# we could use to help improve OCR detection in the event that the above two don't help.
# The next approach I would use is called binarization, which means to separate into two
# distinct parts - in this case, black and white. Binarization is enacted through a process
# called thresholding. If a pixel value is greater than a threshold value, it will be converted
# to a black pixel; if it is lower than the threshold it will be converted to a white pixel.
# This process eliminates noise in the OCR process allowing greater image recognition accuracy.
# With Pillow, this process is straightforward.
# Lets open the noisy impage and convert it using binarization
img = Image.open('readonly/Noisy_OCR.PNG').convert('1')
# Now lets save and display that image
img.save('black_white_noise.jpg')
display(img)

# So, that was a bit magical, and really required a fine reading of the docs to figure out
# that the number "1" is a string parameter to the convert function actually does the binarization.
# But you actually have all of the skills you need to write this functionality yourself.
# Lets walk through an example. First, lets define a function called binarize, which takes in
# an image and a threshold value:
def binarize(image_to_transform, threshold):
    # now, lets convert that image to a single greyscale image using convert()
    output_image=image_to_transform.convert("L")
    # the threshold value is usually provided as a number between 0 and 255, which
    # is the number of bits in a byte.
    # the algorithm for the binarization is pretty simple, go through every pixel in the
    # image and, if it's greater than the threshold, turn it all the way up (255), and
    # if it's lower than the threshold, turn it all the way down (0).
    # so lets write this in code. First, we need to iterate over all of the pixels in the
    # image we want to work with
    for x in range(output_image.width):
        for y in range(output_image.height):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x,y))< threshold: #note that the first parameter is actually a tuple object
                # lets set this to zero
                output_image.putpixel( (x,y), 0 )
            else:
                # otherwise lets set this to 255
                output_image.putpixel( (x,y), 255 )
    #now we just return the new image
    return output_image

# lets test this function over a range of different thresholds. Remember that you can use
# the range() function to generate a list of numbers at different step sizes. range() is called
# with a start, a stop, and a step size. So lets try range(0, 257, 64), which should generate 5
# images of different threshold values
for thresh in range(0,257,64):
    print("Trying with threshold " + str(thresh))
    # Lets display the binarized image inline
    display(binarize(Image.open('readonly/Noisy_OCR.PNG'), thresh))
    # And lets use tesseract on it. It's inefficient to binarize it twice but this is just for
    # a demo
    print(pytesseract.image_to_string(binarize(Image.open('readonly/Noisy_OCR.PNG'), thresh)))

# We can see from this that a threshold of 0 essentially turns everything white,
# that the text becomes more bold as we move towards a higher threshold, and that
# the shapes, which have a filled in grey color, become more evident at higher
# thresholds. In the next lecture we'll look a bit more at some of the challenges
# you can expect when doing OCR on real data

# Tesseract and Photographs
#------------------------------------------------------------------------------------------------------------------

# Lets try a new example and bring together some of the things we have learned.
# Here's an image of a storefront, lets load it and try and get the name of the
# store out of the image
from PIL import Image
import pytesseract
# Lets read in the storefront image I've loaded into the course and display it
image=Image.open('readonly/storefront.jpg')
display(image)
# Finally, lets try and run tesseract on that image and see what the results are
pytesseract.image_to_string(image)

# We see at the very bottom there is just an empty string. Tesseract is unable to take
# this image and pull out the name. But we learned how to crop the images in the
# last set of lectures, so lets try and help Tesseract by cropping out certain pieces.
#
# First, lets set the bounding box. In this image the store name is in a box
# bounded by (315, 170, 700, 270)
bounding_box=(315, 170, 700, 270)

# Now lets crop the image
title_image=image.crop(bounding_box)

# Now lets display it and pull out the text
display(title_image)
pytesseract.image_to_string(title_image)

# Great, we see how with a bit of a problem reduction we can make that work. So now we have
# been able to take an image, preprocess it where we expect to see text, and turn that text
# into a string that python can understand.
#
# If you look back up at the image though, you'll see there is a small sign inside of the
# shop that also has the shop name on it. I wonder if we're able to recognize the text on
# that sign? Let's give it a try.
#
# First, we need to determine a bounding box for that sign. I'm going to show you a short-cut
# to make this easier in an optional video in this module, but for now lets just use the bounding
# box I decided on
bounding_box=(900, 420, 940, 445)

# Now, lets crop the image
little_sign=image.crop((900, 420, 940, 445))
display(little_sign)

# All right, that is a little sign! OCR works better with higher resolution images, so
# lets increase the size of this image by using the pillow resize() function
# Lets set the width and height equal to ten times the size it is now in a (w,h) tuple
new_size=(little_sign.width*10,little_sign.height*10)

# Now lets check the docs for resize()
help(little_sign.resize)

# We can see that there are a number of different filters for resizing the image. The
# default is Image.NEAREST. Lets see what that looks like
display(little_sign.resize( new_size, Image.NEAREST))

# I think we should be able to find something better. I can read it, but it looks
# really pixelated. Lets see what all the different resize options look like
options=[Image.NEAREST, Image.BOX, Image.BILINEAR, Image.HAMMING, Image.BICUBIC, Image.LANCZOS]
for option in options:
    # lets print the option name
    print(option)
    # lets display what this option looks like on our little sign
    display(little_sign.resize( new_size, option))

# From this we can notice two things. First, when we print out one of the resampling
# values it actually just prints an integer! This is really common: that the
# API developer writes a property, such as Image.BICUBIC, and then assigns it to an
# integer value to pass it around. Some languages use enumerations of values, which is
# common in say, Java, but in python this is a pretty normal way of doing things.
# The second thing we learned is that there are a number of different algorithms for
# image resampling. In this case, the Image.LANCZOS and Image.BICUBIC filters do a good
# job. Lets see if we are able to recognize the text off of this resized image

# First lets resize to the larger size
bigger_sign=little_sign.resize(new_size, Image.BICUBIC)
# Lets print out the text
pytesseract.image_to_string(bigger_sign)

# Well, no text there. Lets try and binarize this. First, let me just bring in the
# binarization code we did earlier
def binarize(image_to_transform, threshold):
    output_image=image_to_transform.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x,y))< threshold:
                output_image.putpixel( (x,y), 0 )
            else:
                output_image.putpixel( (x,y), 255 )
    return output_image

# Now, lets apply binarizations with, say, a threshold of 190, and try and display that
# as well as do the OCR work
binarized_bigger_sign=binarize(bigger_sign, 190)
display(binarized_bigger_sign)
pytesseract.image_to_string(binarized_bigger_sign)

# Ok, that text is pretty useless. How should we pick the best binarization
# to use? Well, there are some methods, but lets just try something very simple to
# show how well this can work. We have an english word we are trying to detect, "FOSSIL".
# If we tried all binarizations, from 0 through 255, and looked to see if there were
# any english words in that list, this might be one way. So lets see if we can
# write a routine to do this.
#
# First, lets load a list of english words into a list. I put a copy in the readonly
# directory for you to work with
eng_dict=[]
with open ("readonly/words_alpha.txt", "r") as f:
    data=f.read()
    # now we want to split this into a list based on the new line characters
    eng_dict=data.split("\n")

# Now lets iterate through all possible thresholds and look for an english word, printing
# it out if it exists
for i in range(150,170):
    # lets binarize and convert this to s tring values
    strng=pytesseract.image_to_string(binarize(bigger_sign,i))
    # We want to remove non alphabetical characters, like ([%$]) from the text, here's
    # a short method to do that
    # first, lets convert our string to lower case only
    strng=strng.lower()
    # then lets import the string package - it has a nice list of lower case letters
    import string
    # now lets iterate over our string looking at it character by character, putting it in
    # the comaprison text
    comparison=''
    for character in strng:
        if character in string.ascii_lowercase:
            comparison=comparison+character
    # finally, lets search for comparison in the dictionary file
    if comparison in eng_dict:
        # and print it if we find it
        print(comparison)


# Well, not perfect, but we see fossil there among other values which are in the dictionary.
# This is not a bad way to clean up OCR data. It can useful to use a language or domain specific
# dictionary in practice, especially if you are generating a search engine for specialized language
# such as a medical knowledge base or locations. And if you scroll up and look at the data
# we were working with - this small little wall hanging on the inside of the store - it's not
# so bad.
#
# At this point you've now learned how to manipulate images and convert them into text. In the
# next module in this course we're going to dig deeper further into a computer vision library
# which allows us to detect faces among other things. Then, on to the culminating project!


# Jupyter Widgets (Optional)
#----------------------------------------------------------------------------------------------------------

# In this brief lecture I want to introduce you to one of the more advanced features of the
# Jupyter notebook development environment called widgets. Sometimes you want
# to interact with a function you have created and call it multiple times with different
# parameters. For instance, if we wanted to draw a red box around a portion of an
# image to try and fine tune the crop location. Widgets are one way to do this quickly
# in the browser without having to learn how to write a large desktop application.
#
# Lets check it out. First we want to import the Image and ImageDraw classes from the
# PILLOW package
from PIL import Image, ImageDraw

# Then we want to import the interact class from the widgets package
from ipywidgets import interact

# We will use interact to annotate a function. Lets bring in an image that we know we
# are interested in, like the storefront image from a previous lecture
image=Image.open('readonly/storefront.jpg')

# Ok, our setup is done. Now we're going to use the interact decorator to indicate
# that we want to wrap the python function. We do this using the @ sign. This will
# take a set of parameters which are identical to the function to be called. Then Jupyter
# will draw some sliders on the screen to let us manipulate these values. Decorators,
# which is what the @ sign is describing, are standard python statements and just a
# short hand for functions which wrap other functions. They are a bit advanced though, so
# we haven't talked about them in this course, and you might just have to have some faith
@interact(left=100, top=100, right=200, bottom=200)

# Now we just write the function we had before
def draw_border(left, top, right, bottom):
    img=image.copy()
    drawing_object=ImageDraw.Draw(img)
    drawing_object.rectangle((left,top,right,bottom), fill = None, outline ='red')
    display(img)

'''
Jupyter widgets is certainly advanced territory, but if you would like
to explore more you can read about what is available here: 
https://ipywidgets.readthedocs.io/en/stable/examples/Using%20Interact.html
'''

# Project with Pillow, Tesseract and OpenCV Libraries/Modules Week 3 -------------------------------------------

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


