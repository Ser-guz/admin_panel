import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class GenreFilmwork(UUIDMixin):
    filmwork = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"


class Genre(TimeStampedMixin, UUIDMixin):
    """Жанры фильмов: приключения, фантастика, боевик и т.д."""

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.name


class Filmwork(TimeStampedMixin, UUIDMixin):
    """Фильм"""

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation_date'))
    rating = models.FloatField(
        _('rating'),
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        default=3.5)
    TYPE_CHOICE = (
        ('movies', 'movies'),
        ('tv_show', 'tv_show')
    )
    type = models.CharField(_("type"), max_length=15, choices=TYPE_CHOICE, default="movies")
    genre = models.ManyToManyField(Genre, through=GenreFilmwork, verbose_name=_("genre"))
    certificate = models.CharField(_("certificate"), max_length=512, blank=True)
    file_path = models.FileField(_("file"), blank=True, null=True, upload_to='movies/')

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.title


class Person(UUIDMixin, TimeStampedMixin):
    """Актер или режиссер"""

    full_name = models.CharField(_("name"), max_length=30)

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'актер'
        verbose_name_plural = 'актеры'

    def __str__(self):
        return self.full_name


class PersonFilmwork(UUIDMixin):
    filmwork = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    role = models.TextField(_("role"), null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"

