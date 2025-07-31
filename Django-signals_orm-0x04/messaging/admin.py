from django.contrib import admin
from .models import Message, Notification, MessageHistory

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')
    search_fields = ('content', 'sender__username', 'receiver__username')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    list_filter = ('is_read',)

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('message', 'edited_at', 'edited_by')
    readonly_fields = ('edited_at',)
    search_fields = ('message__content', 'old_content')

