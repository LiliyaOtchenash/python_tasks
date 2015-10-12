from django.db import models

# Create your models here.
class Table(models.Model):
    text_field = models.CharField(max_length=200)
    decimal_field = models.DecimalField(max_digits=12, decimal_places=3)
    def __unicode__(self):
        return self.text_field 

from django.form import ModelForm

class TabeForm(ModelForm):
    class Meta:
        model = Table




    #def __str__(self):
     #   return text_field
    #def __unicode__(self):
     #   return decimal_field   вопросы Андрею
