from django.db import models


# Create your models here.
class ResearchPaper(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
