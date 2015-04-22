from django.contrib import admin
from app.models import One
from backend.admin import admin_site


@admin.register(One, site=admin_site)
class OneAdmin(admin.ModelAdmin):
    list_display = ('id', 'test')