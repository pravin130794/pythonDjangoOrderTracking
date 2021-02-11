
import os

from channels.routing import ProtocolTypeRouter,URLRouter

from channels.auth import AuthMiddlewareStack

from django.urls import path

from django.core.asgi import get_asgi_application

from OrderTracking.consumer import OrderProgress

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OrderTracking.settings')

application = get_asgi_application()


ws_pattern = [
    path('ws/OrderTracking/<order_id>', OrderProgress.as_asgi())
]

application = ProtocolTypeRouter({
    
    "websocket" : AuthMiddlewareStack(URLRouter(
        ws_pattern
    ))
    
})