from django.contrib import admin
from morecode import models

# Register your models here.
admin.site.register(models.Articles)
# 将models创建的表加载到admin后台

