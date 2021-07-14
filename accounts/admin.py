from accounts.models import Investments, userprofile
from django.contrib import admin

# Register your models here.
admin.site.register(userprofile)
admin.site.register(Investments)