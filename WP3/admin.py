from django.contrib import admin

# Register your models here.
from .models import WP3_Questions
admin.site.register(WP3_Questions)

from .models import Testresult_WP3
admin.site.register(Testresult_WP3)

from .models import UserProgress_WP3
admin.site.register(UserProgress_WP3)