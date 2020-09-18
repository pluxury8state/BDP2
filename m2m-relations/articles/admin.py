
from articles.models import Article, NamesSections, Relationship
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

#
# class RelationshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             # В form.cleaned_data будет словарь с данными
#             # каждой отдельной формы, которые вы можете проверить         данные из бд
#             form.cleaned_data
#             # вызовом исключения ValidationError можно указать админке о наличие ошибки
#             # таким образом объект не будет сохранен,
#             # а пользователю выведется соответствующее сообщение об ошибке
#             raise ValidationError('cho')
#         return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    # formset = RelationshipInlineFormset


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        RelationshipInline
    ]


class NameSectionsAdmin(admin.ModelAdmin):
   pass


class RelationshipAdmin(admin.ModelAdmin):
    pass






admin.site.register(Article, ArticleAdmin)

admin.site.register(NamesSections, NameSectionsAdmin)

admin.site.register(Relationship, RelationshipAdmin)
