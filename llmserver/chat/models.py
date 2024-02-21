from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    sender_name = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="sender"
    )
    # receiver_name = models.ForeignKey(
    #     UserProfile, on_delete=models.CASCADE, related_name="receiver"
    # )
    content = models.TextField()
    llm_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
