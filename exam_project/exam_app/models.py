from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2),
                    RegexValidator(regex=r'^[a-zA-Z0-9_]+$',
                                   message='Ensure this value contains only letters, numbers, and underscore.')],
    )
    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
    )


class Album(models.Model):
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'
    GENRES = [(x, x) for x in
              (POP_MUSIC, JAZZ_MUSIC, RB_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)]

    name = models.CharField(
        max_length=30,
        unique=True
    )
    artist = models.CharField(
        max_length=30
    )
    genre = models.CharField(
        max_length=30,
        choices=GENRES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField()
    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )

    class Meta:
        ordering = ['pk']
