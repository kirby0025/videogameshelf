from django.contrib import admin

# Register your models here.

from .models import videoGame
from .models import editor
from .models import manufacturer
from .models import platform

admin.site.register(videoGame)
admin.site.register(editor)
admin.site.register(manufacturer)
admin.site.register(platform)
