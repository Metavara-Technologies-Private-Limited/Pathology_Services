from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Agency)
admin.site.register(Clinic)
admin.site.register(AgencyContact)
admin.site.register(AgencyClinicLinking)
admin.site.register(AgencyServiceLinking)
admin.site.register(Machine)
admin.site.register(Machine_Parameters)
admin.site.register(Pathology_profile)
admin.site.register(Sample)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Parameter)
admin.site.register(ParameterReferenceRange)
admin.site.register(ParameterFormula)
admin.site.register(Template)
admin.site.register(Test)
admin.site.register(By_Parameter)
admin.site.register(By_Template)
admin.site.register(Tube)