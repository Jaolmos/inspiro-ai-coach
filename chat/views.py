"""Vistas para la aplicación de chat."""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from openai import OpenAI
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from .prompts import PROMPT_COACH
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ChatViewSet(viewsets.ModelViewSet):
    """ViewSet para gestionar los chats."""
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retorna solo los chats del usuario actual."""
        return Chat.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Asigna el usuario actual al chat creado."""
        chat = serializer.save(user=self.request.user)
        
        # Crear mensaje del sistema con el prompt inicial
        Message.objects.create(
            chat=chat,
            role='system',
            content=PROMPT_COACH
        )

    @swagger_auto_schema(
        operation_description="Send a message to the coach and receive a personalized response",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'message': openapi.Schema(type=openapi.TYPE_STRING, description='User message')
            }
        ),
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Coach response')
                    }
                )
            )
        }
    )
    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        """Endpoint to send a message and receive a response from the assistant."""
        chat = self.get_object()
        contenido_usuario = request.data.get('message', '')

        # Crear mensaje del usuario
        Message.objects.create(
            chat=chat,
            role='user',
            content=contenido_usuario
        )

        # Obtener historial de mensajes para contexto
        mensajes = Message.objects.filter(chat=chat).order_by('created_at')
        mensajes_formateados = [
            {"role": msg.role, "content": msg.content}
            for msg in mensajes
        ]

        # Llamada a OpenAI
        cliente = OpenAI(api_key=settings.OPENAI_API_KEY)
        try:
            respuesta = cliente.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=mensajes_formateados,
                max_tokens=500,
                temperature=0.7
            )
            
            contenido_asistente = respuesta.choices[0].message.content

            # Guardar respuesta del asistente
            mensaje_asistente = Message.objects.create(
                chat=chat,
                role='assistant',
                content=contenido_asistente
            )

            return Response({
                'message': mensaje_asistente.content
            })

        except Exception as e:
            return Response(
                {'error': 'Error al procesar el mensaje'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )