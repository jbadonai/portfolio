from django.db import models


class Jobs(models.Model):
    choice = [('desktop','Desktop App'), ('web', 'Web App')]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    platform = models.CharField(null=True, choices=choice, max_length=100)

    def __str__(self):
        return self.title
