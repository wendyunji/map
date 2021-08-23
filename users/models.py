from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
# 입력 시 프로필 class - 톤수 범위, 영해 종류 설정할것
class Profile(models.Model):
    class Meta:
        db_table= "user"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    ship_name = models.CharField(null=True, max_length=30) #배 이름
    ship_weight = models.IntegerField(null=True) # 톤수
    ship_type = models.CharField(null=True, max_length=30) #배 종류
    main_activity_territorial_data = models.CharField(null=True,max_length=30) #활동영해
=======
    ship = models.CharField(null=True,max_length=30) #선박 용도
    ship_name=models.CharField(null=True,max_length=40) #선박명
    tonnage = models.CharField(null=True,max_length=30) # 톤수
    month=models.IntegerField(null=True) #월
    active_sea = models.CharField(null=True,max_length=30) #활동영해
    time_f=models.CharField(null=True, max_length=20) #시간


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
>>>>>>> 357cc9a85f1f9b3c9f2cb1ccab8d70f828eed2b9
