from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=26)
    pub_key = models.TextField()

    def __str__(self):
        return self.name

class Message(models.Model):
    uid = str(uuid.uuid4())
    text = models.TextField()
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField('Post date')

    def __str__(self):
       # return self.uid
       return self.uid.split('-')[0]

