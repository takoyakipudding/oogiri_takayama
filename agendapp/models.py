from django.db import models

CATEGORY = (('写真',1),('お題',2))

class Information(models.Model): 
    title = models.CharField(max_length=30)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Answer(models.Model):
    odai = models.ForeignKey(Information, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='topics/', blank=True, null=True)

    def __str__(self):
        return self.title
