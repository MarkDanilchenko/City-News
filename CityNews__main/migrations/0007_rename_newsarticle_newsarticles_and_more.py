# Generated by Django 4.2.7 on 2023-11-12 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CityNews__main', '0006_alter_comment_publish_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsArticle',
            new_name='NewsArticles',
        ),
        migrations.RenameModel(
            old_name='SavedArticle',
            new_name='SavedArticles',
        ),
    ]
