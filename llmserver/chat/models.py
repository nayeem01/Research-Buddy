from django.db import models


# Create your models here.
class UseProfile(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    sender_name = models.ForeignKey(
        UseProfile, on_delete=models.CASCADE, related_name="sender"
    )
    receiver_name = models.ForeignKey(
        UseProfile, on_delete=models.CASCADE, related_name="receiver"
    )
    content = models.TextField()
    llm_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
