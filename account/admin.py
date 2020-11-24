from django.contrib import admin
from .models import User, Content, Tags
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'state',)



class ContentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)

admin.site.register(User, UserAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Tags, TagAdmin)
