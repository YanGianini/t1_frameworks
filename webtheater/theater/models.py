from unicodedata import name
from django.db import models

# Create your models here.
class Categoria():
    def __init__(self, nome=None, desc = None, img=None):
       self._nome = nome
       self._desc = desc
       self._img = img
       self._videos = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_desc(self):
        return self._desc

    def set_desc(self, desc):
        self._desc = desc

    def get_img(self):
        return self._img

    def set_img(self, img):
        self._img = img

    def get_videos(self):
        return self._videos
    
    def add_video(self, video):
        self._videos.append(video)

class Video():
    def __init__(self, id, titulo, urlv, urli, desc, likes, vzl, data_pub):
        self._id = id
        self._titulo = titulo
        self._urlv = urlv
        self._urli = urli
        self._desc = desc
        self._likes = likes
        self._vzl = vzl
        self._data_pub = data_pub

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_urlv(self):
        return self._urlv

    def set_urlv(self, urlv):
        self._urlv = urlv

    def get_urli(self):
        return self._urli

    def set_urli(self, urli):
        self._urli = urli

    def get_desc(self):
        return self._desc

    def set_desc(self, desc):
        self._desc = desc

    def get_likes(self):
        return self._likes

    def set_likes(self, likes):
        self._likes = likes

    def get_vzl(self):
        return self._vzl

    def set_vzl(self, vzl):
        self._vzl = vzl

    def get_data_pub(self):
        return self._data_pub

    def set_vzl(self, data_pub):
        self._data_pub = data_pub
  