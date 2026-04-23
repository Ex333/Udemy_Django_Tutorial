from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Film(models.Model):
    class Category(models.TextChoices):
        ACTION = "action", "Akcja"
        COMEDY = "comedy", "Komedia"
        DRAMA = "drama", "Dramat"
        HORROR = "horror", "Horror"
        THRILLER = "thriller", "Thriller"
        ROMANCE = "romance", "Romans"
        SCI_FI = "sci-fi", "Sci-Fi"
        FANTASY = "fantasy", "Fantasy"
        ANIMATION = "animation", "Animacja"
        DOCUMENTARY = "documentary", "Dokumentalny"
        CRIME = "crime", "Kryminał"
        MYSTERY = "mystery", "Tajemnica"
        ADVENTURE = "adventure", "Przygodowy"
        FAMILY = "family", "Familijny"
        WAR = "war", "Wojenny"
        HISTORY = "history", "Historyczny"
        MUSIC = "music", "Muzyczny"
        SPORT = "sport", "Sportowy"
        WESTERN = "western", "Western"
        BIOGRAPHY = "biography", "Biograficzny"
        

    title = models.CharField(max_length=64, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField()
    category = models.CharField(max_length=20,
                                 choices=Category.choices,
                                   default=Category.ACTION,
                                     verbose_name="Kategoria"
                                     )
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(5)])
    photo = models.ImageField(upload_to="movies_photos", null=True, blank=True)




    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"

    def __str__(self):
        return self.title
   