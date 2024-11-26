"""Configuración del admin para la aplicación de chat."""

from django.contrib import admin
from .models import Chat, Message

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']
    list_filter = ['user', 'created_at']
    search_fields = ['title', 'user__username']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['chat', 'role', 'content', 'created_at']
    list_filter = ['role', 'created_at', 'chat']
    search_fields = ['content', 'chat__title']
