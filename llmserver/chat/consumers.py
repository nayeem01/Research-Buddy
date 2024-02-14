import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from chat.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "public_room"
        self.room_group_name = self.room_name
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        # Leave room group
        await self.disconnect(code)

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data["message"]

        sender = data["sender"]
        print(data)
        text_data_json = json.loads(text_data)

        if "message" in text_data_json:
            message = text_data_json["message"]
            # Save the message to the database
            Message.objects.create(
                content=message, llm_content=message
            )  # Assuming your Message model has a 'content' field

            # Send the message back to the client
            await self.send(text_data=json.dumps({"message": message}))
        else:
            # Handle the case when the required key is missing
            await self.send(
                text_data=json.dumps({"error": 'Missing required key: "message"'})
            )

        # if (
        #     "message" in text_data_json
        #     and "sender_id" in text_data_json
        #     and "receiver_id" in text_data_json
        # ):
        #     message_content = text_data_json["message"]
        #     sender_id = text_data_json["sender_id"]
        #     receiver_id = text_data_json["receiver_id"]

        #     # Retrieve sender and receiver objects
        #     sender = UserProfile.objects.get(id=sender_id)
        #     receiver = UserProfile.objects.get(id=receiver_id)

        #     # Save the message to the database
        #     Message.objects.create(
        #         sender_name=sender,
        #         receiver_name=receiver,
        #         content=message_content,
        #         llm_content=message_content,  # Assuming llm_content is the same as content
        #     )

        #     # Send the message back to the client
        #     await self.send(text_data=json.dumps({"message": message_content}))
        # else:
        #     # Handle the case when the required key is missing
        #     await self.send(
        #         text_data=json.dumps(
        #             {
        #                 "error": 'Missing required key: "message", "sender_id", or "receiver_id"'
        #             }
        #         )
        #     )

    async def chat_message(self, event):
        print(event)
        content = event["message"]
        sender_name = event["sender_username"]
        receiver_name = event["receiver_username"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": content,
                    "sender_name": sender_name,
                    "receiver_name": receiver_name,
                }
            )
        )
