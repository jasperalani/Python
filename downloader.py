""" 
Downloader requires requests and tqdm
$ pip install requests tqdm urllib

https://www.occultboards.com/ebooks/satanism/777.pdf
"""

import urllib
import requests
from tqdm import tqdm
from urllib2 import Request, urlopen, URLError

def get_file_url ():
    url = raw_input('Enter file url: ')
    req = Request(url)
    try:
        response = urlopen(req)
    except URLError, e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            return False
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            return False
    else:
        return url

def download_file (file_url):
    file_name = input("Enter file name: ")
    # Streaming, so we can iterate over the response.
    r = requests.get(file_url, stream=True)
    # Total size in bytes.
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    t=tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(file_name, 'wb') as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    if total_size != 0 and t.n != total_size:
        print("ERROR, something went wrong")

file_url = get_file_url()

if( file_url ): # If successful
    download_file( file_url ) # Download file
else:
    print("Failed to get file url")


# download_file()
