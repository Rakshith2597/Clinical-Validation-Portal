from django.contrib import admin

# Register your models here.

from .models import MR_Likter
admin.site.register(MR_Likter)

from .models import CT_Likter
admin.site.register(CT_Likter)

from .models import XR_Likter
admin.site.register(XR_Likter)

from .models import Testresult_Likter
admin.site.register(Testresult_Likter)

from .models import UserProgress_Likter
admin.site.register(UserProgress_Likter)