from django.contrib import admin

from .models import Student, Teacher, Relationship


class RelationshipInline(admin.TabularInline):
    model = Relationship


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
   inlines = [
       RelationshipInline
   ]