from django.shortcuts import render,redirect
from django.http import HttpResponse
from news.models import Article
from django.db.models import Q
# authentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect



def home(request):
    data=Article.objects.all().order_by('-pub_date')
   
   
    
    return render(request,'home.html',{'articles':data})

# -----NewsDetails--------
def newsdetail(request):
    query = request.GET.get('q')
    print(f"Search query: {query}")  # Print the search query to the console

    if query:
        news_data = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query))
        print(f"Search results: {news_data}")  # Print the search results
    else:
        news_data = Article.objects.all()
        
    context = {'search_data': news_data, 'query': query}
    return render(request, 'newsdetails.html', context)

 
# ---slugnewsDetails------
def newsslugdetail(request,news_slug):
   
    news_data=Article.objects.filter(news_slug=news_slug)
    print(news_data)
    return render(request,'newsslugdetail.html',{'news_slug':news_data})
    


# -----register------
@csrf_protect
def register_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            try:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
            except:
                return render(request,'register.html',{'error':'USername already exists'})
        else:
            return render(request,'register.html',{'error':'Password doesnot match'})
    return render(request,'authentication/register.html')
            
# ------login----
@csrf_protect  
def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('login_home')
        else:
            return render(request,'login.html',{'error':'Invalid credentials'})
    return render(request,'authentication/login.html')
            
# --logout-----
def logout_view(request):
    logout(request)
    return redirect('login')


#----Login-home-----
@login_required
def login_home(request):
    return render(request,'authentication/login-home.html')