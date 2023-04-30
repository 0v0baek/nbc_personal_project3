from django.db import models
from users.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    created_at = models.CharField(max_length=64, default='')
    updated_at = models.CharField(max_length=64, default='')
    completion_at = models.CharField(max_length=64, default='')

    def __str__(self):
        return str(self.title)
