from django.shortcuts import render, redirect
from theater.models import Categoria, Video

# Create your views here.
categoria1 = Categoria('Humor', '', 'laughing.png')
categoria2 = Categoria('Drama', '','theater.png')
categoria3 = Categoria('Automobilistico', '','car.png')
categoria4 = Categoria('Games', '','joystick.png')
categorias = [categoria1, categoria2, categoria3, categoria4]
categoria4.add_video(Video(1, "Elden Ring", " ", " ", "Trailer do jogo Elden Ring"))

def index(request):
    return render(request, "index.html", context={'categorias': categorias})

def content(request, id):
    for categoria in categorias:
        for video in categoria.get_videos():
            if video.get_id() == int(id):
                video_pg = video
                return render(request, "content.html", context={"video": video_pg})

