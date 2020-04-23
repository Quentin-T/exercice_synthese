from django.shortcuts import render, get_object_or_404
from disks.models import album, artist, track

def accueil(request):
    return render(request, 'accueil.html', {'albums': album.objects.all()})

def detail_album(request, id):
    alb = album.objects.get(id=id)
    return render(request, 'album.html', {'alb': alb,'tracks': alb.track_set.all()})
# Create your views here.
