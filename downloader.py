import requests
from tqdm import tqdm

def download_file ():
    file_url = input("Enter file file_url: ")
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

download_file()
