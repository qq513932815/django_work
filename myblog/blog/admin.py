from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'pub_time')
    list_display_links = ('title',)
    list_per_page = 10
    ordering = ('id',)
    list_filter = ('pub_time', )
    search_fields = ('title', 'content')
    # date_hierarchy = 'pub_time'

admin.site.register(Article, ArticleAdmin)
