from django.views.generic import ListView
from django.shortcuts import render
import json
from pprint import pprint
from articles.models import Article
from datetime import datetime
from articles.models import Article
import re

# with open('articles.json', 'r', encoding='utf8') as file:
#     json_data = json.load(file)
#     regex1 = re.compile('(\d{4})-(\d{2})-(\d{2})')
#     regex2 = re.compile('(\d{2}):(\d{2}):(\d{2})')
#
#     for items in json_data:
#         text = items['fields']['text']
#         image = items['fields']['image']
#         date = items['fields']['published_at']
#         title = items['fields']['title']
#         part1 = regex1.findall(date)
#         part2 = regex2.findall(date)
#         new_date = datetime(year= int(part1[0][0]),month= int(part1[0][1]),day= int(part1[0][2]),
#                             hour= int(part2[0][0]),minute= int(part2[0][1]),second= int(part2[0][2]))
#         Article.objects.create(text=text, image=image, published_at=date, title=title)


def articles_list(request):
    template = 'articles/news.html'

    article1 = Article.objects.prefetch_related('relationship_set').prefetch_related('relationship_set__namesections').order_by('published_at')



    context = {
        'object_list': article1,

    }


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
