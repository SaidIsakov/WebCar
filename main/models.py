from django.db import models
#Нужна чтобы модедька обращалась к ссылкам


class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'    
        
    
    
    
    

class Cars(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=150)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year_of_release = models.IntegerField(max_length=4)# год выпуска
    mileage = models.TextField(max_length=15)#         Пробег
    PTC = models.TextField(max_length=20)#             ПТС
    owner = models.IntegerField(max_length=1)#        Владелец
    сondition = models.TextField(max_length=10)#     Состояние
    power = models.TextField(max_length=10)#         Мощность
    engine_capacity = models.TextField(max_length=10)# ⁡обьем двигателя
    engine_type = models.TextField(max_length=10)#    ⁡⁢⁣⁢Тип двигателя⁡
    transmission_box = models.TextField(max_length=20) #Коробка передач⁡
    drive = models.TextField(max_length=20)#
    Equipment = models.TextField(max_length=20)#      Комплектация
    Body_type = models.TextField(max_length=10)#      Тип кузова
    colour = models.TextField(max_length=10)
    wheel = models.TextField(max_length=10)#            Руль
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'