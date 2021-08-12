from django.db import models

class Task(models.Model):
    task=models.CharField(max_length=100)
    completed=models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.task