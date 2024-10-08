# Generated by Django 3.2.25 on 2024-10-05 19:46

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('news', '0002_remove_newsitem_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItemTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('image', models.ImageField(blank=True, upload_to='categories/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='NewsTaggedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_newstaggeditem_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='news.newsitemtag', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='taggeditem',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='taggeditem',
            name='tag',
        ),
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ['-priceNew'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='newsitem',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Доступно'),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='old_priceNew',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Старая цена'),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='priceNew',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Новая цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsitem',
            name='slug',
            field=models.CharField(default=0, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='items/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='NewsTag',
        ),
        migrations.DeleteModel(
            name='TaggedItem',
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='tagged_items', through='news.NewsTaggedItem', to='news.NewsItemTag', verbose_name='Категории'),
        ),
    ]
