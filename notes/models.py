from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.


class Cathegory(models.Model):
    label = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Cathegories'

    def __unicode__(self):
        return self.label


# # Solution including manually creating forms
# class Note(models.Model):
#     RATING_CHOICES = zip(range(1, 11), range(1, 11))

#     description = models.TextField()
#     url = models.TextField()
#     rating = models.IntegerField(choices=RATING_CHOICES,
#                                  blank=True, null=True)
#     cathegory = models.ForeignKey(Cathegory, blank=True, null=True)

#     def __unicode__(self):
#         return self.description


class Note(models.Model):
    RATING_CHOICES = zip(range(1, 11), range(1, 11))

    description = models.TextField()
    url = models.TextField()
    # TODO: Try specifying the widget using the 'widget' keyword
    # url = models.TextField(widget=forms.TextInput)
    rating = models.IntegerField(choices=RATING_CHOICES,
                                 blank=True, null=True)
    cathegory = models.ForeignKey(Cathegory, blank=True, null=True)

    def __unicode__(self):
        return self.description


class NoteForm(ModelForm):
    """Auto generated form to generate Note models."""
    class Meta:
        model = Note


    def __unicode__(self):
        return self.description

