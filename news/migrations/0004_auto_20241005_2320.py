# Generated by Django 3.2.25 on 2024-10-05 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20241005_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='old_priceNew',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='priceNew',
        ),
    ]