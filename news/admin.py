from django.contrib import admin
from .models import Category, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date','img')
    list_filter = ('category', 'pub_date')
    search_fields = ('title',)

class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
