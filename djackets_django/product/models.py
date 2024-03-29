from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''

    def get_thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail.url
        if self.image:
            self.thumbnail = self.make_thubnail(self.image)
            self.save()
            return self.thumbnail.url
        return ''

    def make_thubnail(self, image, size=(300, 200)):
        _image = Image.open(image)
        _image.convert('RGB').thumbnail(size)

        thumb = BytesIO()
        _image.save(thumb, 'JPEG', quality=85)

        thumbnail = File(thumb, name=image.name)

        return thumbnail
