from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Custom Validators


def validate_hindi(value):
    # Test for Hindi Unicode Range
    # https://stackoverflow.com/questions/19704317/how-to-detect-unicode-character-range-in-python
    # by Martijn Pieters
    maxchar = max(value)
    if u'\u0900' <= maxchar <= u'\u097f':
        pass
    else:
        raise ValidationError(
            _('%(value)s is not unicode Hindi'),
            params={'value': value},
        )

# Models for the Hindi Script App


class Word(models.Model):
    hindi = models.CharField(max_length=64, validators=[validate_hindi])
    roman = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.hindi} ({self.roman})"


class Level(models.Model):
    """ The Game Level Number """
    level_number = models.SmallIntegerField()
    words = models.ManyToManyField(Word, blank=False, related_name="words")

    def __str__(self):
        return str(self.level_number)
