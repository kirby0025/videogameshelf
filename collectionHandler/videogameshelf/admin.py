from django.contrib import admin

# Register your models here.

from .models import videoGame
from .models import editor

admin.site.register(videoGame)
admin.site.register(editor)
