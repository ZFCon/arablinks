import random,string

def generator(num = 10, char = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for _ in range(num))

def create_code(instance):
    new_code = generator()
    klass = instance.__class__
    qs_exists = klass.objects.filter(short_code = new_code).exists
    if qs_exists:
        return generator()
    return new_code