# Generated by Django 3.1.1 on 2020-09-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200916_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='namessections',
            name='is_main',
            field=models.BooleanField(null=True),
        ),
    ]
