from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kursus(models.Model):
    nama = models.CharField(max_length=50)
    gambar = models.FileField(upload_to="static/")
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Siswa(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    no_handphone = models.CharField(max_length=50)

    def __str__(self):
        return self.nama


class Belajar(models.Model):
    user = models.ForeignKey(User,on_delete=models.RESTRICT)
    kursus = models.ForeignKey(Kursus,on_delete=models.RESTRICT)
    tanggal = models.DateField()
    status = models.BooleanField()
    link = models.TextField()
    
