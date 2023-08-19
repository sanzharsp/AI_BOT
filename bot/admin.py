from django.contrib import admin
from .models import *


class UserIdModelAdmin(admin.ModelAdmin):

    model = UserId
    list_display = ('user_id', 'created_at', 'updated_at')
    list_filter = ('user_id', 'created_at', 'updated_at')
    search_fields = ('user_id',)
    ordering = ('user_id',)


class MessageTextModelAdmin(admin.ModelAdmin):

    model = MessageText
    list_display = ('user_id', 'created_at',)
    list_filter = ('user_id__user_id', 'created_at',)
    search_fields = ('user_id__user_id',)
    ordering = ('user_id',)

class SystemTextModalModelAdmin(admin.ModelAdmin):

    model = SystemTextModal
    list_display = ('id','created_at', 'updated_at')
    list_filter = ('id','created_at', 'updated_at')
    search_fields =  ('id','created_at', 'updated_at')
    ordering =  ('id','created_at', 'updated_at')

admin.site.register(MessageText, MessageTextModelAdmin)
admin.site.register(UserId, UserIdModelAdmin)
admin.site.register(SystemTextModal, SystemTextModalModelAdmin)
