from django.db import models
from .machine import Machine

class Parameter(models.Model):

    TYPE_CHOICES = [
        ('NUMERIC', 'Numeric'),
        ('TEXT', 'Text'),
    ]
    UNIT_CHOICES = [
        ('ml', 'ML'),
        ('g_dl', 'g/dL'),
        ('mg_dl', 'mg/dL'),
    ]
    parameter_code = models.CharField(max_length=50)
    parameter_name = models.CharField(max_length=100)
    parameter_print_name = models.CharField(max_length=100, null=True, blank=True)
    type_of_value = models.CharField(max_length=10, choices=TYPE_CHOICES)
    parameter_unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    delta_check_percentage = models.FloatField(null=True, blank=True)
    technique_used = models.CharField(max_length=100, null=True, blank=True)
    skip_numeric_result_entry = models.BooleanField(default=False)
    execution_calendar_linking = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parameterreferenceranger= models.ForeignKey('ParameterReferenceRange', on_delete=models.CASCADE, related_name='reference_ranges')

    class Meta:
        db_table = "Parameter"

    def __str__(self):
        return self.parameter_name
    

class ParameterReferenceRange(models.Model):

    CATEGORY_CHOICE=[
        ('MALE', 'male'),
        ('FEMALE','female')
    ]
    machine= models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='machine_reference')
    category= models.CharField(max_length=20, choices=CATEGORY_CHOICE)
    min_ref=models.FloatField()
    max_ref=models.FloatField()
    min_authz=models.FloatField()
    max_authz=models.FloatField()
    is_age_applicable=models.BooleanField(default=False)
    age_lower_limit=models.IntegerField()
    age_upper_limit=models.IntegerField()
    improbable_value_1=models.FloatField(null=True, blank=True)
    improbable_value_2= models.FloatField(null=True, blank=True)
    is_reflex= models.BooleanField(default=False)
    reflex_value_1=models.FloatField(null=True,blank=True)
    reflex_value_2=models.FloatField(null=True, blank=True)
    panic_value_1=models.FloatField(null=True,blank=True)
    panic_value_2=models.FloatField(null=True,blank=True)
    varying_ref_range=models.TextField(null=True,blank=True)
    notes=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ParameterReferenceRange"

    def __str__(self):
        return self.parameter.parameter_name
    

class ParameterFormula(models.Model):

    formula_expression = models.TextField()
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, related_name='formula')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





    