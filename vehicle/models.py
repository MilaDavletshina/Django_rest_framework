from django.db import models

from config import settings


# Задача 1
class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    #10.1
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


# Задача 2
class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    # 10.1
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


# Задача 3
class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True, related_name='milage') # related_name чтобы можно было обращаться не через milage_set, а просто через milage
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, blank=True, null=True, related_name='milage')

    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.PositiveSmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
        ordering = ('-year',) # "-"  означает в обратную сторону