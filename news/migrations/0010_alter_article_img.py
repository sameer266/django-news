# Generated by Django 5.0.7 on 2024-07-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_article_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='news_images/'),
        ),
    ]
