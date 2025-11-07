from django.db import models

class Tasks(models.Model):
    gender = {
        '1': 'male',
        '2': 'famale',
    }

    name = models.CharField(max_length=128)
    description = models.TextField()
    gender_type = models.CharField(choices=gender.items(), default='2')
    
    def __str__(self):
        return f" {id} - {self.name}"

