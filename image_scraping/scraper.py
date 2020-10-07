import requests
import json
import concurrent.futures

def temp(arg):
    image = requests.get(arg['url'], stream=True).content

    file_path = 'images/'+ str(arg['filename']) + '.jpg'
    with open(file_path, 'wb') as file:
        file.write(image)
        file.close()

def download_from_url(urls, searchword):
    with concurrent.futures.ThreadPoolExecutor() as excecutor:
        for idx, url in enumerate(urls):
            excecutor.submit(temp, {'url': url, 'filename': searchword + str(idx)})  


def unsplash_img(searchword='cake'):
    pageURL = 'https://api.unsplash.com/search/photos?client_id=CxLGfT5uIdlU0WRaI_1vSVBg--L62BWOex9Okz5Le_g&per_page=100&query=' + searchword
    response = requests.get(pageURL)
    json_data = json.loads(response.text)

    urls = []
    for result in json_data['results']:
        url = result['urls']['full']
        urls.append(url)
        
    
    download_from_url(urls[:60], searchword)

import time

if __name__ == '__main__':
    s = time.time()
    unsplash_img('cake')
    e = time.time()
    print(e-s)





