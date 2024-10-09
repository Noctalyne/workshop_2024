from django.contrib import admin

# Register your models here.

from .models import User, UserTutor, UserPathology, Pathology, HealthMeasurements

admin.site.register(User)
admin.site.register(UserTutor)
admin.site.register(UserPathology)
admin.site.register(Pathology)
admin.site.register(HealthMeasurements)
