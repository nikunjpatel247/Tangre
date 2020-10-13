from django.db import models

# Create your models here.

choice = (
    ('all','all'),
    ('brand','brand'),
    ('img-man','img-man'),
    ('creative','creative'),
    ('web','web'),
    ('print-mat','print-mat')
)
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    choice = models.CharField(max_length=10, default="all", choices=choice)

    def __str__(self):
        return self.title