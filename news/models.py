from django.db import models
from  autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    news_slug=AutoSlugField(populate_from='title',default=None,null=True,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    img=models.ImageField(upload_to='news_images/', null=True,blank=True)

    def __str__(self):
        return self.title
