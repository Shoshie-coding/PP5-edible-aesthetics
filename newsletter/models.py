from django.db import models


class NewsletterUser(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email