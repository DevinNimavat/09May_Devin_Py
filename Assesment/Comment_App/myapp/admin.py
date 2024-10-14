from django.contrib import admin

from myapp.models import CommentData

# Register your models here.
class CommentDataAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id','name','email','post_id','body']

admin.site.register(CommentData)