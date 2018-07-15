from django.contrib import admin
from .models import User, Post, LikeDislike, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ('title', 'views')

    ordering = ('-views',)


# Register your models here.
admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(LikeDislike)
admin.site.register(Comment)
