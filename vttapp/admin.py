from django.contrib import admin

# Register your models here.
from .models import MR
admin.site.register(MR)

from .models import XR
admin.site.register(XR)

from .models import CT
admin.site.register(CT)