from django.contrib import admin
from .models import Article, Editor, Tags


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register([Editor, Tags])
admin.site.register(Article, ArticleAdmin)
