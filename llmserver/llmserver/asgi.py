import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "llmserver.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # WebSocket chat handler
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
