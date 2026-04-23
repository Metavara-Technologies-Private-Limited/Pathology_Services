from django.db import models
from .clinic import Clinic 

class Agency(models.Model):
    specializations = models.ManyToManyField("Specialization", related_name="agencies")
    clinics = models.ManyToManyField("Clinic", related_name="agencies")
    agency_code = models.CharField(max_length=50, unique=True)
    agency_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    address_line_1 = models.TextField(null=True, blank=True)
    address_line_2 = models.TextField(null=True, blank=True)
    address_line_3 = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.agency_name
    
    
class AgencyContact(models.Model):
    agency = models.ForeignKey('Agency', on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class meta:
        db_table="AgencyContact"


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class meta:
        db_table="Specialization"

    
class AgencyServiceLinking(models.Model):
    agency = models.ForeignKey("Agency", on_delete=models.CASCADE, related_name="agency_services")
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.agency} - {self.service} - {self.rate}"
    

class AgencyClinicLinking(models.Model):
    agency = models.ForeignKey("Agency", on_delete=models.CASCADE, related_name="agency_links")
    clinic = models.ForeignKey("Clinic", on_delete=models.CASCADE, related_name="clinic_links")
