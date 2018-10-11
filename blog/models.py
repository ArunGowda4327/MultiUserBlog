from django.db import models

from django.utils import timezone
from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='img/', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)


    #add this when you are adding createview
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})





    def __str__(self):
        return self.title




class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()


    #add this when you are adding commentview
    def get_absolute_url(self):
        return reverse('post_list')




    def __str__(self):
        return self.text
