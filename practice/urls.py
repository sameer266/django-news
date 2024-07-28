from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('<news_slug>/', views.newsslugdetail, name='newshomedetail'), 
    path('news/', include('news.urls')),
    
    path('newsdetail/', views.newsdetail, name="newsdetail"),
    path('newsdetail/<news_slug>/', views.newsslugdetail, name="newsslugdetail"),
    
    # ----register----login
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    
    # logout
    path('logout/', views.logout_view, name="logout"),
    
    path('login-home/', views.login_home, name="login_home")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
