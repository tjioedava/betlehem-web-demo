from django.db import models

class Ibadah(models.Model):
    ibadah_ke = models.IntegerField(default = 0)
    hari = models.CharField(max_length = 255, default = '')
    jam_mulai = models.CharField(max_length = 255, default = 'mulai')
    jam_selesai = models.CharField(max_length = 255, default = 'selesai')

    def __str__(self):
        return f'Ibadah {self.ibadah_ke} ({self.hari} {self.jam_mulai}-{self.jam_selesai})'
    
    class Meta:
        verbose_name_plural = 'Ibadah'

class Extensi(models.Model):
    nama = models.CharField(max_length = 255)
    alamat = models.TextField()
    ibadah = models.ManyToManyField(Ibadah)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = 'Extensi'

class Komunitas(models.Model):
    nama = models.CharField(max_length = 255)
    gembala_wilayah = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = 'Komunitas'


