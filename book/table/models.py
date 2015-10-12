from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Table(models.Model):
    text = models.CharField(max_length=200)
    decim = models.DecimalField(max_digits=12, decimal_places=3)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('table', kwargs={'pk': self.pk})

class TabForm(ModelForm):
    class Meta:
        model = Table
        fields = ['text', 'decim'] 
