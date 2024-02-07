import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.send(text_data=json.dumps({"message": "You are now connected!"}))

    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]
            self.send(text_data=json.dumps({"message": message}))
            self.close()
            self.close(code=4123)
        except json.JSONDecodeError:
            print(f"Invalid JSON: {text_data}")

    def disconnect(self, close_code):
        pass

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))
