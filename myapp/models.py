from django.db import models

# Create your models here.
class Records(models.Model):
    record_id=models.IntegerField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id}{self.record_id}{self.first_name} {self.last_name}"