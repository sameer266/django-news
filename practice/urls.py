from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('login-home/', views.login_home, name="login_home"),
    path('news/', include('news.urls')),
    path('newsdetail/', views.newsdetail, name="newsdetail"),
    path('newsdetail/<news_slug>/', views.newsslugdetail, name="newsslugdetail"),
    
    #  i put this url at last beacause
    # Example Conflict:
# If a user navigates to /register/, Django will match it with <news_slug>/ before it gets a chance to match it with path('register/', views.register_view, name="register").
# This results in the newsslugdetail view being called with news_slug='register'.
    path('<news_slug>/', views.newsslugdetail, name='newshomedetail'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
