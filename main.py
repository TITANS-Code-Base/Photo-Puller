import threading
import requests
import concurrent.futures

def download_photo(n):
    data=requests.get("https://picsum.photos/200")
    with open (f"photos/image{n}.jpeg", "wb") as f:
        f.write(data.content)


with concurrent.futures.ThreadPoolExecutor() as e:
    e.map(download_photo, range(15))