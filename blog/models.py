from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now())
    published_date = models.DateField(blank=True, null=True)

    # Sets 'published_date' to time of publishing.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Returns a String with a title for the post.
    def __str__(self):
        return self.title
