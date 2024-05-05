from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    image = models.ImageField("Зображення", upload_to='articles/', blank=True, null=True)
    created_date = models.DateTimeField("Дата створення", default=timezone.now)
    modified_date = models.DateTimeField("Дата редагування", auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "публікація"
        verbose_name_plural = "публікації"

class Monument(models.Model):
    MONUMENT_TYPES = [
        ('history', "Історичні об'єкти культурної спадщини"),
        ('architecture', 'Споруди культового призначення'),
        ('archeology', "Археологічні об'єкти культурної спадщини"),
        ('reservation', 'Державні історико-культурні заповідники та музеї'),
    ]

    name = models.CharField("Назва", max_length=200)
    description = models.TextField("Опис")
    image = models.ImageField("Зображення", upload_to='monuments/', blank=True, null=True)
    location = models.CharField("Локація", max_length=255)
    latitude = models.DecimalField("Широта", max_digits=9, decimal_places=6)
    longitude = models.DecimalField("Довгота", max_digits=9, decimal_places=6)
    monument_type = models.CharField("Тип", max_length=50, choices=MONUMENT_TYPES)
    foundation_date = models.CharField("Дата заснування", max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "історична пам'ятка"
        verbose_name_plural = "історичні пам'ятки"

