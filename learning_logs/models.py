from django.db import models
# Class allowing user to create topic 
class Topic(models.Model):
    """ A topic the user is learning about """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returning a string """
        return self.text
