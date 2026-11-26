import os
from django.core.exceptions import ValidationError

def validate_avatar_size(image):
    max_size = 8 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError('Картинка не должна быть больше 8 МБ')

def avatar_upload_path(instance, filename):
    return os.path.join('avatars', str(instance.user.id), filename)



