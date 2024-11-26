"""Serializadores para la aplicación de chat."""

from rest_framework import serializers
from .models import Chat, Message

class MessageSerializer(serializers.ModelSerializer):
    """Serializador para los mensajes."""
    class Meta:
        model = Message
        fields = ['id', 'role', 'content', 'created_at']

class ChatSerializer(serializers.ModelSerializer):
    """Serializador para los chats."""
    messages = MessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Chat
        fields = ['id', 'title', 'messages', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']