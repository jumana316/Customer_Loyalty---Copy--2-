from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timezone


# class signup(models.Model):
#     username = models.CharField(max_length=50, null=True)
#     u_email = models.EmailField(max_length=50, null=True)
#     phone = models.CharField(max_length=50, null=True)
#     password = models.CharField(max_length=50, null=True)
#     c_password = models.CharField(max_length=50, null=True)

#     class Meta:
#         verbose_name = 'Customer'
#         verbose_name_plural = 'Customers'
    
#     def __str__(self):
#         return f'{self.username}'


class User(AbstractUser):
    email = models.EmailField(("email address"), blank=True, unique=True)
    phone = models.CharField(max_length=15)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'


class CustomerDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    total_points = models.IntegerField(default=0)
    last_redeemed = models.DateTimeField(null=True, blank=True)

class Reward(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards', null=True)
    points = models.IntegerField(null=True)
    # signup = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards', null=True)
    
    def __str__(self):
        return f'{self.username} ( {self.points} )'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    reward_points = models.IntegerField(default=0, null=True)







# class RewardCatalog(models.Model):
#     name = models.ForeignKey(Reward, on_delete=models.CASCADE, null=True)
#     points_required = models.IntegerField()

#     def redeem_reward(user, reward_catalog_id):
#         reward_catalog = RewardCatalog.objects.get(id=reward_catalog_id)
#         if user.reward_set.filter(points__gte=reward_catalog.points_required).exists():
#             reward = user.reward_set.create(points=-reward_catalog.points_required)
#             return reward
#         return None
#     def __str__(self):
#         return f'{self.name} - {self.points_required}'
    
    

