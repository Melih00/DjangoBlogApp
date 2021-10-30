from django.contrib import admin
from .models import Comments, Like, Posts, User
# Register your models here.

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Like)