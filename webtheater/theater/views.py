from django.shortcuts import render, redirect
from theater.models import Categoria, Video
from dados import categorias


def index(request):
    return render(request, "index.html", context={'categorias': categorias})

def content(request, id):
    for categoria in categorias:
        for video in categoria.get_videos():
            if video.get_id() == int(id):
                video_pg = video
                return render(request, "content.html", context={"video": video_pg})

