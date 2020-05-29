from django.db import models

# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    #Needed to tell how the items in the database to be listed(what their name should be)
    def __str__(self):
        return self.item + ' | ' + str(self.completed)