from django.contrib import admin
from .models import Dog, Toy, Feeding


# Register your models here.
admin.site.register(Dog)
admin.site.register(Toy)
admin.site.register(Feeding)