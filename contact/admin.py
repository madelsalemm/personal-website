from atexit import register
import site
from django.contrib import admin
from .models import Info , Portfolio , ProfileImage , Skill
# Register your models here.

admin.site.register(Info)
admin.site.register(Portfolio)
admin.site.register(ProfileImage)
admin.site.register(Skill)