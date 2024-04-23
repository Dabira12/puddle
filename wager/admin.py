from django.contrib import admin

# Register your models here.
from .models import Sport

admin.site.register(Sport)
from .models import Wager

admin.site.register(Wager)
