from django.contrib import admin

from .models import Post, PostCategory, AdvancedUser


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'slug', 'created_time')
    prepopulated_fields = {'slug': ('title',)}


class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, CategoryPostAdmin)
admin.site.register(AdvancedUser)