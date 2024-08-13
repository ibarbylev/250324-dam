"""Задача: скачать к себе на компьютер 100 последних фотографий
со страницы Explore | Flickr: https://www.flickr.com/explore/

Это один из самых популярных фото-хостингов в интернете с множеством
классных фотографий от фотографов со всего мира.

Разобьём задачу на две части:
 - Вывести URL всех картинок.
   (Пример URL: https://live.staticflickr.com/65535/53534030316_e8e655393a_w.jpg)

 - Скачать каждую картинку по ее URL и сохранить ее на диске.

ВАЖНО: Нужные нам картинки имеют аттрибут loading="lazy".
Отфильтруйте ненужные картинки и скачивайте только нужные.
"""
from pprint import pprint

import requests
from local_settings import API_KEY


SEARCH_QUERY = 'dogs'
URL = f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={API_KEY}&text={SEARCH_QUERY}&format=json&nojsoncallback=1'


data = ...  # (json object)


photos = data['photos']['photo']
foto_urls = []
for photo in photos:
    photo_id = photo['id']
    farm_id = photo['farm']
    server_id = photo['server']
    secret = photo['secret']

    photo_url = f'https://farm{farm_id}.staticflickr.com/{server_id}/{photo_id}_{secret}.jpg'
    foto_urls.append(photo_url)

