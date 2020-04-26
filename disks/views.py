from django.shortcuts import render, redirect, get_object_or_404
from disks.models import album, artist, track
from .forms import RechercheForm

alb = album.objects.all()


def accueil(request):
    alb = album.objects.all()

    form = RechercheForm(request.POST or None)

    if form.is_valid():
        champ = form.cleaned_data['con']
        alb1 = album.objects.filter(track__Name__contains=champ)
        alb2 = album.objects.filter(Title__contains=champ)
        alb3 = album.objects.filter(artist__Name__contains=champ)
        alb = set([i for i in alb1] + [i for i in alb2] + [i for i in alb3])

        return render(request, 'accueil.html', locals())

    return render(request, 'accueil.html', locals())


def detail_album(request, id):
    alb = album.objects.get(id=id)
    return render(request, 'album.html', {'alb': alb, 'tracks': alb.track_set.all()})
# Create your views here.
