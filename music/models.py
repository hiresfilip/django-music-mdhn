from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Type name",
                            help_text='Enter a type of musical instrument')
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Instrument(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    history = models.TextField(blank=True, null=True, verbose_name="History")
    type = models.ManyToManyField(Type, help_text='Select a type for this instrument')

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instrument-detail', args=[str(self.id)])

def attachment_path(instance, filename):
    return "film/" + str(instance.film.id) + "/attachments/" + filename