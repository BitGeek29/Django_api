from django.contrib import admin

# Register your models here.
from .models import ApiModel


@admin.register(ApiModel)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')