from django.db import models
from django.db.models import TextChoices


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.TextField(null=True, blank=True, verbose_name='Изображение',)
    relation = models.ManyToManyField('NamesSections', related_name='sections', through='Relationship')


    def __str__(self):
        return f'Загаловок: {self.title}, текст: {self.text}, дата:{self.published_at}, изображение:{self.image}'


class Sections(TextChoices):
    Culture = 'Культура', 'Культура'
    City = 'Город', 'Город'
    Health = 'Здоровье', 'Здоровье'
    Science = 'Наука', 'Наука'
    Space = 'Космос', 'Космос'
    IR = 'Международные отношения', 'Международные отношения'


class NamesSections(models.Model):
    name_of_section = models.TextField(choices=Sections.choices)



    def __str__(self):
        return f'{self.name_of_section}'


class Relationship(models.Model):

    namesections = models.ForeignKey(NamesSections, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, null=False)

    #
    # class Meta:
    #     verbose_name = 'Статья'
    #     verbose_name_plural = 'Статьи'
    #
    # def __str__(self):
    #     return self.title
