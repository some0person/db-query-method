from sys import argv
from requests import get
from threading import Thread, local
import concurrent.futures


def get_request(destination):
    get(destination)
    print(f"Successfull get request")


if __name__ == "__main__":
    local_thread = local()
    URL = argv[1]
    while True:
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=16)
        print("Starting requests...")
        for i in range(16):
            pool.submit(get_request, URL)
        
        pool.shutdown(wait=True)
    
    