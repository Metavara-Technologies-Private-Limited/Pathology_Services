from django.contrib import admin

from .models import *

from restapi.models.test_template import (
    Template,
)

from restapi.models.test_test import (
    Test,
    TestParameter,
    TestTemplate,
    TestSample,
)

from restapi.models.test_category import (
    Category,
)

from restapi.models import (
    Pathology_profile,
)

# Configuration Masters
admin.site.register(Agency)
admin.site.register(Machine)
admin.site.register(Pathology_profile)
admin.site.register(Sample)
admin.site.register(Category)
admin.site.register(Parameter)
admin.site.register(ParameterReferenceRange)
admin.site.register(Test)
admin.site.register(Tube)
admin.site.register(Template)
admin.site.register(TestParameter)
admin.site.register(TestTemplate)
admin.site.register(TestSample)
admin.site.register(Clinic)
admin.site.register(AgencyClinic)

# Shipment Module
admin.site.register(Patient)
admin.site.register(PendingShipment)
admin.site.register(ShipmentShipped)
admin.site.register(ShipmentReceived)
admin.site.register(ActivityLogs)

# Collection Module
admin.site.register(Collection)