from django.contrib import admin
from .models import publicLIKE,publicCOMMENT,publicPOST
# Register your models here.

admin.site.register(publicLIKE)
admin.site.register(publicCOMMENT)
admin.site.register(publicPOST)