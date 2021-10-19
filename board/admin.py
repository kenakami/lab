from django.contrib import admin

# Register your models here.

from .models import Thread, Post

class PostInline(admin.TabularInline):
    model = Post

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('time', 'last_updated', 'subject')
    list_filter = ('time', 'last_updated')
    inlines = [PostInline]
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('time', 'comment')
    #list_filter = ('time')
    pass

