# Generated by Django 3.1.1 on 2020-09-16 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_remove_namessections_relation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('namesections', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='articles.namessections')),
            ],
        ),
        migrations.AddField(
            model_name='namessections',
            name='relation',
            field=models.ManyToManyField(related_name='sections', through='articles.Relationship', to='articles.Article'),
        ),
    ]