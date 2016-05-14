from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(max_length=200, default="None")
    password = models.CharField(max_length=200)
    bio = models.CharField(max_length=200, default="None")
    location = models.CharField(max_length=200, default="None")
    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)
