from django.db import models

class product(models.Model):
    İsim = models.CharField(max_length=100)
    Fiyat = models.IntegerField()
    Açıklama = models.TextField(blank=True)
    Resim = models.FileField(upload_to='dokumanlar/',null=True,blank=True)


    def __str__(self):
        return self.name
