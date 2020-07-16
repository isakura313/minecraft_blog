from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') #какие свойства отображались
    list_filter = ('status', 'created', 'publish', 'author') #по каким свойствам это все фильтруется
    prepopulated_fields = {'slug' : ('title',)}  #связанные колонки
    raw_id_fields = ('author',) #получаем информацию из БД База Данных
    date_hierarchy = 'publish' # порядок от нового к старым
    ordering = ('status', 'publish') #можно менять порядок по статусу и по публикации


# Register your models here.