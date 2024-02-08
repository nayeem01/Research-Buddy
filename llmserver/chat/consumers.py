import json
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
<<<<<<< Updated upstream
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
=======
        self.room_name = 'public_room'
        self.room_group_name = self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )


    def receive(self, text_data):
        json_text = json.loads(text_data)
        message = json_text["message"]
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chat_message", 
                "message": message
            }
        )
    
    def chat_message(self, event):
        message = event['message']
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
>>>>>>> Stashed changes
