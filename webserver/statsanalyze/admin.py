from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AllTimeEntry)
admin.site.register(MonthEntry)
admin.site.register(WeekEntry)
admin.site.register(Agent)
admin.site.register(User)