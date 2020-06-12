import tqdm
import requests

import urllib
import requests
from tqdm import tqdm
from urllib2 import Request, urlopen, URLError

def __main__ ():

    nw()

    # Retreive required inputs
    file_url = raw_input('Enter file url: ')
    file_name = raw_input('Enter file name\n(leave blank for automatic file name generation): ')
    file_location = raw_input('Enter file save location: ')

    # Verify url is valid
    req = Request(file_url)
    try:
        response = urlopen(req)
    except URLError, e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:

        # URL is valid, download file

        if(file_name == 'a' or file_name == 'auto'):
            file_name = file_url.rsplit('/', 1)[1] # Retreive file name from the end of the url
        
        r = requests.get(file_url, stream=True) # Streaming, so we can iterate over the response.

        total_size = int(r.headers.get('content-length', 0)) # Total size in bytes
        block_size = 1024 #1 Kilobyte
        t=tqdm(total=total_size, unit='iB', unit_scale=True)

        with open(file_location + file_name, 'wb') as file_to_write:
            for data in r.iter_content(block_size):
                t.update(len(data))
                file_to_write.write(data)
                t.close()
                if total_size != 0 and t.n != total_size:
                    print("ERROR, something went wrong")

                # print("Downloaded file to: " + file_location) # Success
                
                # nw()

def nw(amt = 1, pr = 0) :
    newline = '\n'
    newline_string = ''
    for amount in range(amt):
        newline_string += newline
    if(pr == 0):
        print(newline_string)
    elif(pr == 1):
        return newline_string

if(__name__ == '__main__'):
    __main__()