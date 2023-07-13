from django.db import models
from django.core.exceptions import ValidationError

def validate_file_type(value):
    # Check if the file has a valid file extension
    valid_extensions = ['jpg', 'png', 'jpeg']

    file_extension = value.name.split('.')[-1]
    print(file_extension)
    if file_extension.lower() not in valid_extensions:
        raise ValidationError("Invalid file type. Only images allowed.")

def validate_file_size(value):
    # Check if the file size is within the allowed limit (in bytes)
    allowed_size = 2*1024*1024  # 2 MB
    if value.size > allowed_size:
        raise ValidationError("File size exceeds the allowed limit of 2 MB.")


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Image(models.Model):
    src = models.FileField(validators=[validate_file_type, validate_file_size])
    album = models.ForeignKey(Album, on_delete= models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.album.title}/{self.src}'
