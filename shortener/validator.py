from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def clean_url(value):
    urlv = URLValidator()
    try:
        if 'http' not in str(value):
            value = 'http://' + str(value)
            urlv(value)
            return value
        else:
            urlv(value)
    except:
        raise ValidationError("Use a real URL")
    return value