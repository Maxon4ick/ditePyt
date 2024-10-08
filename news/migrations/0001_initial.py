# Generated by Django 3.2.25 on 2024-09-17 11:28

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('image', models.ImageField(blank=True, upload_to='news/categories/', verbose_name='Изображение Новости')),
                ('description', models.TextField(blank=True, verbose_name='Описание Нвоости')),
            ],
            options={
                'verbose_name': 'Категория Новости',
                'verbose_name_plural': 'Категории Новостей',
            },
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_taggeditem_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemsNews', to='news.newstag', verbose_name='Категория Новости')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название Новости')),
                ('description', models.TextField(verbose_name='Описание Новости')),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления новости')),
                ('image', models.ImageField(blank=True, upload_to='itemsNews/', verbose_name='Изображение')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='tagged_News_items', through='news.TaggedItem', to='news.NewsTag', verbose_name='Категории Новостей')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
