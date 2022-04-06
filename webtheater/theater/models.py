from unicodedata import name
from django.db import models

# Create your models here.
class Categoria():
    def __init__(self, nome=None, img=None):
       self._nome = nome
       self._img = img
       self._videos = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_img(self):
        return self._img

    def set_img(self, img):
        self._img = img

    def get_videos(self):
        return self._videos
    
    def add_video(self, video):
        self._videos.append(video)