from django.urls import path
from . import views
urlpatterns = [
    path('',views.accueil,name='accueil'),
    path('album/<int:id>', views.detail_album, name='detail'),
]