from django.db import models
from ckeditor.fields import RichTextField
 
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
