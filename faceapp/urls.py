from django.urls import path
from . import views

urlpatterns = [
    # path('indexs/', views.indexs, name='indexs'),
    path('', views.index, name='index'),
    path('<int:facedb_id>/', views.detail, name='detail'),
    # path('capture/', views.capture, name='capture'),
    # path('train/', views.train, name='train'),
    # path('recognise/', views.recog, name='recog'),
    path('thank/', views.thanks, name='thanks'),
]