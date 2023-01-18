from django.db import models

# Create your models here.
class Project(models.Model): # Имя таблицы
    title = models.CharField(max_length=100) #поле title, символьное поле, заголовок не длиннее 100 сиволов
    description = models.TextField() # описание, может хранить много символов
    technology = models.CharField(max_length=50) # описываются технологии. Ограничение 50 символов
    image = models.FileField(upload_to='img/') # поле с файлом и этот файл сохранен в папке img/
