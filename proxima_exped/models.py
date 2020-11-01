from django.db import models


class Expedition(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()
    cover_photo = models.ImageField(blank=True, upload_to='proxima_exped/images/')
    description = models.TextField(max_length=255)
    url = models.URLField(blank=True)
    inclusives = models.TextField(default='Transport, Water')
    person_price = models.IntegerField()
    account_no = models.IntegerField(default=0o72715)
    account_name = models.CharField(max_length=24, default='PROXIMA')

    def __str__(self):
        return self.title

