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
    ship_name = models.CharField(null=True, max_length=30) #배 이름
    ship_weight = models.IntegerField(null=True) # 톤수
    ship_type = models.CharField(null=True, max_length=30) #배 종류
    main_activity_territorial_data = models.CharField(null=True,max_length=30) #활동영해