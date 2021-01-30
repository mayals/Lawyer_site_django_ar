from blog_app.models import Comment
from django.contrib.auth.models import User, Group
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from PIL import Image

# ---- PROFILE MODEL ----#
class Profile(models.Model):
    user_key = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name = 'profile_to_user')
    
    prof_image = models.ImageField(
        verbose_name='صورة شخصية',
        help_text='أختر صورة رمزية تمثلك',
        upload_to='prof_images/%Y/%m/%d/',
        default='default_user.png',
        null=True)

    prof_created = models.DateTimeField(
        verbose_name='تاريخ إنشاء الملف الشخصي',
        auto_now_add=True,
        auto_now=False,
        null=True)

    prof_updated = models.DateTimeField(
        verbose_name='تاريخ آخر تحديث للملف الشخصي',
        auto_now_add=False,
        auto_now=True,
        null=True)


    prof_mob = models.CharField(
        verbose_name='رقم الجوال',
        max_length=14,
        help_text='ضع رقم الجوال بالصيغة الدولية مثلا (جوال سعودي 00966501234567)',
        unique=True,
        blank=False,
        null=True)


    Gender_choices = [
        ('M', 'ذكر'),
        ('F', 'أنثى'),
    ]
    gender = models.CharField(
        verbose_name='الجنس',
        max_length=10,
        choices=Gender_choices,
        null=True,
        blank=True)

    def __str__(self):
            return f'الملف الشحصي ل {self.user_key.username}'


    #inside Profile class we put function to decresse image that user insert in the profile model: 
    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

            img = Image.open(self.prof_image.path)
            if img.width > 300 or img.height > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.prof_image.path)



#### end of Profile model(class)   #####




# this function out side profile class >> inside models file
# ---------(out class function) to doing Signal --------------------------------------------------------------------------#
# do function to creating proile automatically when user create his account register ------

def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user_key=kwargs['instance'])

# post_save to call the above function and connect it with sender :
post_save.connect(create_profile, sender=User)

# --------------------------------------------------------------------------------
#طريقة أحمد أبو عيسى __ بالضبط نفس طريقة محمود روؤف أعلاه ه  -- work ok ادناه

# def create_profile(sender, **kwarg):
#     if kwarg['created']:
#         Profile.objects.create(user=kwarg['instance'])

# post_save.connect(create_profile, sender=User)
# ----------------------------------------------------------

# -- 'طريقة محمد عيسى المشروع الجديد .. يعمل ملف خارجي به دالة تعمل  السكنال 

# def customer_create_profile(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.get(name="customer")
#         instance.groups.add(group)

#         Customer.objects.create(
#             user=instance,
#             name=instance.username
#         )

#         print('Customer profile created ! ')


# post_save.connect(customer_create_profile, sender=User)
