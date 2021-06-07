from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),
    #path('de',views.detail,name='detail')
    #path('show.html',views.show, name='show')
    
]