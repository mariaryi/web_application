from django.db import models

class Education(models.Model):
    full_name = models.CharField(max_length=200, default="Рябцева Мария Дмитриевна")
    photo = models.ImageField(upload_to='pyscripts/static/img/', blank=True, null=True)
    email = models.EmailField(default="mdryabtseva@edu.hse.ru")
    phone = models.CharField(max_length=20, default="+9 999 999-99-99")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name