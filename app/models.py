from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import magic

# Create your models here.
ext_validator =  FileExtensionValidator(['png','jpg','jpeg'])

def validate_mime_type(file):
    accept = ['image/png', 'image/jpg', 'image/jpeg']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)

    if file_mime_type not in accept:
        raise ValidationError("Unsupported File Type.")

def validate_file_size(value):
    # Check if the file size is within the allowed limit (in bytes)
    allowed_size = 2*1024*1024  # 2 MB
    if value.size > allowed_size:
        raise ValidationError("File size exceeds the allowed limit of 2 MB.")

class Gallery(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# class Title(models.Model):
#     title = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.title

# class Image(models.Model):
#     images = models.ImageField(upload_to='', validators=[ext_validator,validate_mime_type,validate_file_size])

#     album = models.ForeignKey(Title, on_delete= models.CASCADE, related_name='images')

#     def __str__(self):
#         return f'{self.album.title}/{self.images}'
