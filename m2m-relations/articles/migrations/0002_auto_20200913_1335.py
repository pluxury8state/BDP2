# Generated by Django 3.1.1 on 2020-09-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.TextField(blank=True, null=True, verbose_name='Изображение'),
        ),
    ]
