# 24.7.2. Implementation of the requests_with_caching module
'''
You may find it useful to understand how this module works. The source code is not very complicated; we’ve reproduced
it below. You can use it as a template for implementing code for your own caching pattern in other settings.

Note
This module is not available outside this textbook; in a full python environment you won’t be able to install a
requests_with_caching module. But you can copy the code and make it work outside the textbook environment.

Note
We have optimized this code for conceptual simplicity, so that it is useful as a teaching tool. It is not very efficient,
 because it always stores cached contents in a file, rather than saving it in memory. If you are ever implementing
 the caching pattern just for the duration of a program’s run, you might want to save cached content in a
 python dictionary in memory rather than writing it to a file.

The basic idea in the code is to maintain the cache as a dictionary with keys representing API requests that have
been made, and values representing the text that was retrieved. In order to make our cache live beyond one program
execution, we store it in a file. Hence, there are helper functions _write_to_file and read_to_file that write a
cache dictionary to and read it from a file.

In order for the textbook to provide a cache file that can’t be overwritten, we distinguish between the permanent file,
 which is provided as part of the online textbook, and a temporary cache file that will live only until the page is
 reloaded.
'''

import requests
import json

PERMANENT_CACHE_FNAME = "permanent_cache.txt"
TEMP_CACHE_FNAME = "this_page_cache.txt"

def _write_to_file(cache, fname):
    with open(fname, 'w') as outfile:
        outfile.write(json.dumps(cache, indent=2))

def _read_from_file(fname):
    try:
        with open(fname, 'r') as infile:
            res = infile.read()
            return json.loads(res)
    except:
        return {}

def add_to_cache(cache_file, cache_key, cache_value):
    temp_cache = _read_from_file(cache_file)
    temp_cache[cache_key] = cache_value
    _write_to_file(temp_cache, cache_file)

def clear_cache(cache_file=TEMP_CACHE_FNAME):
    _write_to_file({}, cache_file)

def make_cache_key(baseurl, params_d, private_keys=["api_key"]):
    """Makes a long string representing the query.
    Alphabetize the keys from the params dictionary so we get the same order each time.
    Omit keys with private info."""
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get(baseurl, params={}, private_keys_to_ignore=["api_key"], permanent_cache_file=PERMANENT_CACHE_FNAME, temp_cache_file=TEMP_CACHE_FNAME):
    full_url = requests.requestURL(baseurl, params)
    cache_key = make_cache_key(baseurl, params, private_keys_to_ignore)
    # Load the permanent and page-specific caches from files
    permanent_cache = _read_from_file(permanent_cache_file)
    temp_cache = _read_from_file(temp_cache_file)
    if cache_key in temp_cache:
        print("found in temp_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        return requests.Response(temp_cache[cache_key], full_url)
    elif cache_key in permanent_cache:
        print("found in permanent_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        return requests.Response(permanent_cache[cache_key], full_url)
    else:
        print("new; adding to cache")
        # actually request it
        resp = requests.get(baseurl, params)
        # save it
        add_to_cache(temp_cache_file, cache_key, resp.text)
        return resp

# Question: requests-7-1: Why is it important to use a function like make_cache_key in this caching pattern rather
# than justusing the full url as the key?
# Answer: Because when requests.get encodes URL parameters, the keys in the params dictionary might be in any order,
# which would make it hard to compare one URL to another later on, and you could cache the same request multiple times.

# Comparing the strings "rowling&harry+potter" and "harry+potter&rowling", they are different as far as Python is
# concerned, but they are the same as far as meaning to a REST API is concerned! That's why we need to manipulate these
# strings carefully to always get the same, canonical key for the cache dictionary.

