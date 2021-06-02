from django.db import models
from users.models import CustomUser
from django.urls import reverse

class Todo(models.Model):
    task = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['completed', 'due_date']
        

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('list')
