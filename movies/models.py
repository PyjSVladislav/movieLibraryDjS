from django.db import models
from datetime import date

class Category(models.Model):
    
    name = models.CharField("Category", max_length = 150)
    description = models.TextField("Description")
    url = models.SlugField(max_length = 160, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):

    name = models.CharField("Name", max_length = 100)
    age = models.PositiveSmallIntegerField("Age", default = 0)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to = "actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor and director"
        verbose_name_plural = "Actors and directors"


class Genre(models.Model):

    name = models.CharField("Name", max_length = 100)
    description = models.TextField("Description")
    url = models.SlugField(max_length = 160, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    

class Movie(models.Model):

    title = models.CharField("Title", max_length = 100)
    tagline = models.CharField("Tagline", max_length = 100, default = "")
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to = "movies/")
    year = models.PositiveSmallIntegerField("Release date", default = 2019)
    country = models.CharField("Country", max_length = 50)
    directors = models.ManyToManyField(Actor, verbose_name = "director", related_name = "film_director")
    actors = models.ManyToManyField(Actor, verbose_name = "actors", related_name = "film_actor")
    genres = models.ManyToManyField(Genre, verbose_name = "genres")
    world_premiere = models.DateField("World Premiere", default = date.today)
    budget = models.PositiveIntegerField("Budget", default = 0, help_text = "point in dollars")
    fees_in_usa = models.PositiveIntegerField("Fees in USA", default = 0, help_text = "point in dollars")
    fees_in_world = models.PositiveIntegerField("Fees in world", default = 0, help_text = "point in dollars")
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, verbose_name = "Category")# при удалении категории во всех связанных фильмах будет установаленно null
    url = models.SlugField(max_length = 160, unique = True)
    draft = models.BooleanField("Draft", default = False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShot(models.Model):

    title = models.CharField("Title", max_length = 100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to = "movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name = "Movie", on_delete = models.CASCADE) #при удалении фильма все связанные кадры тоже удаляться

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "MovieShot"
        verbose_name_plural = "MovieShots"


class RatingStar(models.Model):

    value = models.SmallIntegerField("Value", default = 0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "RatingStar"
        verbose_name_plural = "RatingStars"


class Rating(models.Model):

    ip = models.CharField("IP adress", max_length = 25)
    star = models.ForeignKey(RatingStar, on_delete = models.CASCADE, verbose_name = "star")
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, verbose_name = "movie")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Review(models.Model):

    email = models.EmailField()
    name = models.CharField("Name", max_length = 100)
    text = models.TextField("Text", max_length = 5000)
    parent = models.ForeignKey(
        'self', verbose_name = "parent", on_delete = models.SET_NULL, blank = True, null = True
        ) #запись будет ссылаться на запись в этой же таблице
    movie = models.ForeignKey(Movie, verbose_name = "movie", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"