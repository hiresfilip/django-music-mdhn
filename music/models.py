from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


def attachment_path(instance, filename):
    return "figures/" + str(instance.instrument.id) + "/attachments/" + filename

def poster_path(instance, filename):
    return "figures/" + str(instance.id) + "/poster/" + filename


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
    """ Zde mi to hlásí chybu, že nesná poster_path, ale proč? Vždy o několik řádků níž je poster_path definován. """
    poster = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Poster")
    type = models.ManyToManyField(Type, help_text='Select a type for this instrument')

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instrument-detail', args=[str(self.id)])

class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")

    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )

    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True, default='image', help_text='Select allowed attachment type', verbose_name="Attachment type")
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-last_update", "type"]

    def __str__(self):
        return f"{self.title}, ({self.type})"

