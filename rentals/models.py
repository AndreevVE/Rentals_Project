from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

#Типы жилья
class PropertyType(models.TextChoices): #TextCoices для перечислений enum
    #Админка:
    apartment = "Apartment", "Квартира"
    house = "house", "Дом"
    studio = "studio", "Студия"
    room = "room", "Комната"

#Объявления
class Listing(models.Model):
    #это владелец объявления(Арендодатель), ForeignKey: связь многие к одному, у одного пользователя может быть много объявлений
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    #заголовок, описание, город/район
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)

    #Цена, комнаты, тип жилья:
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveIntegerField() #только положительное число
    property_type = models.CharField(max_length=20, choices=PropertyType.choices)

    #Активный статус
    is_active = models.BooleanField(default=True)#позволяет скрывать объявление, не удаляя его

    #Служебные поля:
    created_at = models.DateField(auto_now_add=True)#авто. сохраняет дату создания
    veiws = models.PositiveIntegerField(default=0)#счётчик просмотров объявлений

def __str__(self):
    return self.title


