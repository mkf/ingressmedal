from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Entry)
admin.site.register(Agent)
admin.site.register(User)