
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news import views
from practice import views as practice_views
urlpatterns = [ 
               
               path('national/',views.national,name="national"),
               path('national/<news_slug>/',practice_views.newsslugdetail),
               
               path('sport/',views.sport,name="sport"),
               path('sport/<news_slug>/',practice_views.newsslugdetail),
               
               
               path('politics/',views.politics,name="politics"),
               path('politics/<news_slug>/',practice_views.newsslugdetail),
               
               path('money/',views.money,name="money"),
               path('money/<news_slug>/',practice_views.newsslugdetail)
               
               ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)