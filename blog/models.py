from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from datetime import date
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,username,password, **kwargs):
        if not username:
            raise ValueError('username not valid')
      
        user = self.model(username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_superuser',True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('super user must have is_staff true')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('super user must have is_superuser true')
        if kwargs.get('is_active') is not True:
            raise ValueError('super user must have is_active true')
        
        return self.create_user(username,password,**kwargs)
    
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)
    profile_pic = models.ImageField(upload_to='media/profile_pics',default='tatlikedi.jpeg')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.username
class Posts(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE,related_name='creator')
    title = models.CharField( max_length=70)
    image =  models.ImageField(upload_to='media/post_images',default='post_images/amugus.gif')
    content = models.TextField()
    last_updated = models.TimeField( auto_now=True)
    shared = models.TimeField( auto_now_add=True)
    today = date.today()
    today = today.strftime("%B %d")
    # shared = models.DateTimeField(auto_now_add=True,)
    
    CATEGORY=(
        ('IT','IT'),
        ('General Culture','General Culture'),
        ('Games','Games'),
        ('Fashion','Fashion'),
        ('Humor','Humor'),
        ('Movies','Movies'),
        ('Chatting','Chatting'),
        ('Others','Others'),
    )
    category = models.CharField(default='Django', max_length=50 , choices=CATEGORY)
    liked = models.ManyToManyField(User, default=0,blank=False, related_name='liked')
    views = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.creator} - {self.title}'   
    def num_likes(self):
        return self.liked.all().count()
    class Meta:
        ordering = ['-id']
class Comments(models.Model):
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    shared_post = models.ForeignKey(Posts, on_delete=models.CASCADE,blank=True,null=True)
    comment = models.TextField()
    share_time = models.TimeField( auto_now=False, auto_now_add=True)
    REQUIRED_FIELDS = []
    def __str__(this):
        return f'{this.shared_by} | '
class Like(models.Model):
    choices=LIKE_CHOICES= (
        ('like','Like'),
        ('unlike','Unlike')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=50)
    def __str__(self):
        return str(self.post)