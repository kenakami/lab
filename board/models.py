from django.db import models
from django.urls import reverse

# Create your models here.

class Thread(models.Model):
    subject = models.TextField(blank=True)
    time = models.DateTimeField('time', auto_now_add=True)
    #original_post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    last_updated = models.DateTimeField('last_updated')
    id = models.BigAutoField(primary_key=True)

    class Meta:
        ordering = ['-last_updated']

    def get_absolute_url(self):
        # return reverse('feed')
        return reverse('thread-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.id} - {self.subject}'

class Post(models.Model):
    thread = models.ForeignKey('Thread', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField('time', auto_now_add=True)
    comment = models.TextField()
    name = models.TextField(blank=True)
    

    class Meta:
        ordering = ['time']

    '''
    def get_absolute_url(self):
        return reverse('thread', args=[str(self.id)])
    '''

    def __str__(self):
        return f'{self.id}'

