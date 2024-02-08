import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
<<<<<<< Updated upstream
from django.urls import path
=======
>>>>>>> Stashed changes
from chat.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "llmserver.settings")

<<<<<<< Updated upstream
django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
=======

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
>>>>>>> Stashed changes
        # websocket connection
        # WebSocket chat handler
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
