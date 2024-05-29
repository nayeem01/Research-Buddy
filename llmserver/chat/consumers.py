import json
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from chat.models import Message


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send(
            {
                "type": "websocket.accept",
            }
        )

    async def websocket_receive(self, event):
        # receive message from websocket
        print("Receive=========", event)
        print("Receive=========", event["text"])

        # sending message to client
        await self.send(
            {
                "type": "websocket.send",
                "text": "message send to client",
            }
        )

    async def websocket_disconnect(self, event):
        print("Disconnected", event)
        raise StopConsumer()
