from django.contrib import admin
from .models import*
from restapi.models.test_template import (
    Template,
    TemplateParameter
)
from restapi.models.test_test import Test
from restapi.models.test_category import Category
from restapi.models import Pathology_profile

# Register your models here.
admin.site.register(Agency)
#admin.site.register(Clinic)
#admin.site.register(AgencyContact)
#admin.site.register(AgencyClinicLinking)
#admin.site.register(AgencyServiceLinking)
admin.site.register(Machine)
#admin.site.register(Machine_Parameters)
admin.site.register(Pathology_profile)
admin.site.register(Sample)
#admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Parameter)
admin.site.register(ParameterReferenceRange)
admin.site.register(Test)
admin.site.register(Tube)
admin.site.register(Template)
admin.site.register(TemplateParameter)
admin.site.register(TestParameter)
admin.site.register(TestTemplate)
admin.site.register(TestSample)
admin.site.register(Clinic)
admin.site.register(AgencyClinic)