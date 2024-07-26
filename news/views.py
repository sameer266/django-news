from django.shortcuts import render
from news.models import Category,Article

# Create your views here.
# ------National--------
def national(request):
    data=""
    try:
        national_category=Category.objects.get(name="national")
        data=Article.objects.filter(category=national_category).order_by('-pub_date')
    except(Exception) as e:
        print("National category not found")
    data={'news_data':data}
    return render(request,'national.html',data)


# ------Sport----------
def sport(request):
    data=""
    try:
        sport_category=Category.objects.get(name="sports")
        data=Article.objects.filter(category=sport_category).order_by('-pub_date')
    except(Exception) as e:
        print("Sport category not found")
    data={'news_data':data}
    return render(request,'sport.html',data)

# ------Politics-----------
def politics(request):
    data=""
    try:
        politics_category=Category.objects.get(name="politics")
        data=Article.objects.filter(category=politics_category).order_by('-pub_date')
    except(Exception) as e:
        print("politics caregory not found")
    data={'news_data':data}
    return render(request,'politics.html',data)


# -------Money---------------
def money(request):
    news={}
    try:
        money_category=Category.objects.get(name="money")
        data=Article.objects.filter(category=money_category).order_by('-pub_date')
        
        news={'news_data':data}
    except (Exception) as e:
        print("error")
    return render(request,'money.html',news)


