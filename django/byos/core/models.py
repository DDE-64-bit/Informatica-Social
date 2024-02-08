from django.db import models

from django.contrib.auth import get_user_model

user = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    
    def __str__(self):
        return self.user.username