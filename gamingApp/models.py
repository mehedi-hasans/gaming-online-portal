from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1, 'Administrator'),
        (2, 'Game Developer'),
        (3, 'Gaming Portal'),
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class GameModel(models.Model):
    name= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    gameImage = models.ImageField(upload_to='media/Game')

    def __str__(self):
        return self.name
    



from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']






# class GamingPortal(models.Model):
#     name = models.Model.CaharField(max_lenght)
#     description = models.Model.Charfield(max)
#     image = models.ImageField
    
# class DeveloperModel(models.Model):
#     name = models.Charfield(max_length=100)
#     developer_site_name = models.CharField(max_length=80)
#     developer_description = models.CharField(max_length=50)
#     developer_email= models.EmailField

# class AdministratiorPortal(models.Model):
#     administratorName = models.CharField(max_length=20)
#     administratorEmail = models.EmailField(max_length=30)









































    
# class Course(models.Model):
#     name= models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    
# class SessionYear(models.Model):
#     session_start = models.CharField(max_length=100)
#     session_end = models.CharField(max_length=100)

#     def __str__(self):
#         return self.session_start + '-' + self.session_end
    

# class Student(models.Model):
#     admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     address=models.TextField()
#     gender = models.CharField(max_length=100)
#     courseid = models.ForeignKey(Course, on_delete=models.DO_NOTHING,default=1)  # Set the default course
#     sessionyearid = models.ForeignKey(SessionYear, on_delete=models.DO_NOTHING,default=1)
#     cratedat = models.DateTimeField(auto_now_add=True)  # Set the default value using timezone.now
#     updateat = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.admin.first_name + " " + self.admin.last_name
    


# class Teacher(models.Model):
#     admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     address=models.TextField()
#     gender = models.CharField(max_length=100)
#     mobile=models.CharField(max_length=100)
#     courseid = models.ForeignKey(Course, on_delete=models.DO_NOTHING,default=2)
#     experience=models.CharField(max_length=100)
#     cratedat = models.DateTimeField(auto_now_add=True)  # Set the default value using timezone.now
#     updateat = models.DateTimeField(auto_now=True)
       
#     def __str__(self):
#         return self.admin.first_name + " " + self.admin.last_name
