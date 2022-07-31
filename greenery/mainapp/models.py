from django.db import models
from django.urls import reverse

# Create your models here.

class Greenery(models.Model):
    title = models.CharField(verbose_name="название", max_length=128)
    description = models.TextField(verbose_name="описание")
    photos = models.ImageField(verbose_name="фото", upload_to="images/%Y/%m/%d/")
    created_at = models.DateTimeField(verbose_name="добавлено", auto_now_add=True)


    def __str__(self):
        return self.title.capitalize()

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title', 'created_at']
    




