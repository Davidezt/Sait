# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
#
# class User(AbstractUser):
#     is_seller = models.BooleanField(default=False, verbose_name='Seller')
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def save(self, *args, **kwargs):
#         from services.products_module.models import Currency
#
#         super().save(*args)
#
#
# class UserAddress(models.Model):
#     country = models.CharField(max_length=255, verbose_name='Country')
#     city = models.CharField(max_length=255, verbose_name='City')
#     address = models.CharField(max_length=255, verbose_name='Address')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_address')
#
#
# class UserSettings(models.Model):
#     currency = models.ForeignKey('products_module.Currency',
#                                  on_delete=models.CASCADE,
#                                  verbose_name='Currency',
#                                  related_name='user_settings')
#     send_push = models.BooleanField(default=True, verbose_name='Send Push')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_settings')


from django.contrib.auth.models import AbstractUser
from django.db import models
from services.products_module.models import Currency

class User(AbstractUser):
    is_seller = models.BooleanField(default=False, verbose_name='Seller')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class UserAddress(models.Model):
    country = models.CharField(max_length=255, verbose_name='Country')
    city = models.CharField(max_length=255, verbose_name='City')
    address = models.CharField(max_length=255, verbose_name='Address')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_address')


class UserSettings(models.Model):
    currency = models.ForeignKey('products_module.Currency',
                                 on_delete=models.CASCADE,
                                 verbose_name='Currency',
                                 related_name='user_settings')
    send_push = models.BooleanField(default=True, verbose_name='Send Push')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_settings')
