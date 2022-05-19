from django.db import models
# Class allowing user to create topic 
class Topic(models.Model):
    """ A topic the user is learning about """
    text = models.CharField(max_length=200) #allocating 200 spaces in database
    date_added = models.DateTimeField(auto_now_add=True) #automatically sets date to topic upon creation

    def __str__(self):
        """ Returning a string """
        return self.text

class Entry(models.Model):
    """ Something specific about topic """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #connects e/a entry with its topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) #allows for timestamps on e/a entry

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """ Return string representing of model """
        if len(self.text) > 50:
            return f"{self.text[:50]}..." #showing first 50 characters of text
        else:
            return f"{self.text}"
