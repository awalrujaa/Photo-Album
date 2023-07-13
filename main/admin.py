from django.contrib import admin
from .models import Image, Album
# from .models import Image, Album
# Register your models here.

admin.site.register(Album)
admin.site.register(Image)