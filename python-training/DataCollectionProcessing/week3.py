# 24. Internet APIs: write computer programs that access data,  process the data in useful ways,
# even from multiple sources

# 24.6.1. Fetching in python with requests.get
import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
#page = requests.get("https://presence.com.ng/index.php/blog")
print(type(page))
print(page.text[:150]) # print the first 150 characters
#print(page.text) # print whole page
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results

# Make a HEAD request to a web page, and return the HTTP headers:
import requests
#the required first parameter of the 'head' method is the 'url':
#x = requests.head('https://www.w3schools.com/python/demopage.php')
x = requests.head('https://presence.com.ng/index.php/blog')
#print the response headers (the HTTP headers of the requested file):
print(x.headers)

import requests
d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)
'''
The get function in the requests module takes an optional parameter called params. If a value is specified for that 
parameter, it should be a dictionary. The keys and values in that dictionary are used to append something to the URL 
that is requested from the remote site.
'''

'''
an executable sample, using the optional params parameter of requests.get. It gets the same data from the datamus api 
that we saw previously. Here, however, the full url is built inside the call to requests.get; we can see what url was 
built by printing it out, on line 5.
'''
import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched

# requests-6-1: How would you request the URL http://bar.com/goodstuff?greet=hi+there&frosted=no
# using the requests module?
requests.get("http://bar.com/goodstuff", params = {'greet': 'hi there', 'frosted':'no'})
# note: The ? and & are added automatically, and the space in hi there is automatically encoded as %3A.

# requests-6-2: If resp is a Response object returned by a call to requests.get(),
# write some ways to extract the contents into a python dictionary or list?
'''
A. resp.json()
B. json.loads(resp.text)
'''

#--------------------Runestone textbook special function---------------------------------#
import requests
# it's not found in the permanent cache
res = requests.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
print(res.text[:100])
# this time it will be found in the temporary cache
res = requests.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# This one is in the permanent cache.
res = requests.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")
#------------------------------------------------------------------------------------------

# Using REST APIs

# Fetching a Page Google
import requests
d = {'q': 'bobby and chisom', 'tbm':'isch'}
results = requests.get('https://google.com/search', params = d)
print(results.url)
print(results.text)

# Fetching a Page Yandex
import requests
d = {'q': 'bobby and chisom', 'tbm':'isch'}
results = requests.get('https://yandex.com/search', params = d)
print(results.url)
print(results.text)

# Fetching a Page Duckduckgo
import requests
d = {'q': 'bobby and chisom', 'tbm':'isch'}
results = requests.get('https://duckduckgo.com/search', params = d)
print(results.url)
print(results.text)

# 24.8.2. Defining a function to make repeated invocations
'''
Suppose you were writing a computer program that was going to automatically translate paragraphs of text into 
paragraphs with similar meanings but with more rhymes. You would want to contact the datamuse API repeatedly, 
passing different values associated with the key rel_rhy. Let’s make a python function to do that. 
You can think of it as a wrapper for the call to requests.get.
'''
# import statements for necessary Python modules
import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    #return resp.json() # Return a python object (a list of dictionaries in this case)
print(get_rhymes("funny"))
print(get_rhymes("dash"))

# Challenge: try using the datamuse API to actually make a paragraph translator!
#_--------------------------------------------------------------------------------------------------------------------
# requests-8-1: Why would you define a function in order to make a request to a REST API for data?
# -> Because that means you have to write less repeated code if you want to make a request to the same API more than
#     once in the same program.
# -> Writing functions to complete a complex process in your code makes it easier to read and easier to fix later.
# -> Because a lot of things stay the same among different requests to the same API.
#--------------------------------------------------------------------------------------------------------------------
# requests-8-1: If the results you are getting back from a call to requests.get() are not what you expected,
# what’s the first thing you should do?
# -> look at the first few characters of the .text attribute of the Response object

# requests-8-2: In a full python environment, if there is a runtime error and you don’t get a Response object back
# from the call to requests.get(), what should you do?
# -> invoke the requestURL() function with the same parameters you used to invoke requests.get()

# requests-8-3: In the runestone environment, if there is a runtime error and you don’t get a Response object back from
# the call to requests.get(), what should you do?
# -> look at the values you passed in to requests.get()
'''
Generally, a runtime error when you invoke ``requests.get`` in the Runestone environment is caused by the value of the
 ``params`` parameter not being a dictionary, or not having only strings as keys and values.
'''

#  make a request to the iTunes API
import requests
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters,permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)

# using  Understand. Extract. Repeat. . For example, to print out the names of all the podcasts returned 
import requests
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters, permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)
for r in py_data['results']:
    print(r['trackName'])

# Below is some code that queries the flickr API for images that have a particular tag.
# import statements
import requests_with_caching
import json
# import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'yourkeyhere'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests.get(baseurl, params = params_diction, permanent_cache_file="flickr_cache.txt")
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(flickr_resp.url) # Paste the result into the browser to check it out...
    return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")
# Some code to open up a few photos that are tagged with the mountains and river tags...
photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    # webbrowser.open(url)

# requests-11-1: If you wanted to search for photos tagged with either river or mountains, rather than requiring both,
# what would you change in the code? (Hint: check the documentation)
# -> tag_mode (Optional)
# Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.

# requests-12-1: When you have non-ASCII characters in a string and you get an error trying to write them, which
# method should you invoke on the string?
# -> encode()
#   It's a little counter-intuitive, since it seems like you already have an encoding of the information, but you have to
#   re-encode it by substituting sequences of ASCII characters for some of the Unicode characters

# requests-12-2: In the textbook environment, what should you do if you are unable to write data to a file
# because of a Unicode encoding error?
