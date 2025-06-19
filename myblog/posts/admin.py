from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    search_fields = ("title", "body", "author__username")  # Enables search by title, body, or author's username
    list_filter = ("author", "date")

admin.site.register(Post, PostAdmin)