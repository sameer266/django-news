# Generated by Django 5.0.7 on 2024-07-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(default=None, null=True, upload_to='news_image/ '),
        ),
    ]
