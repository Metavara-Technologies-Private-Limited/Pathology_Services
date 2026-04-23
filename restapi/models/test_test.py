from django.db import models
from .test_category import Category
from .test_parameter import Parameter
from .tube import Tube
from .test_category import Category
from .service import Service
from .sample import Sample



class Test(models.Model):

    REPORT_TYPE_CHOICES = [
        ('parameter', 'Parameter'),
        ('template', 'Template'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="test_category" )
    tube= models.ForeignKey(Tube, on_delete=models.CASCADE, related_name="tests_service")
    service=models.ForeignKey(Service, on_delete=models.CASCADE, related_name="tests_service")

    test_code = models.CharField(max_length=50, unique=True)
    test_name = models.CharField(max_length=100)
    print_name = models.CharField(max_length=150, null=True, blank=True)
    service_name = models.CharField(max_length=150, null=True, blank=True)
    tube_name = models.CharField(max_length=150, null=True, blank=True)
    test_completion_time = models.CharField(max_length=10, null=True, blank=True)
    is_sensitive = models.BooleanField(default=False)
    suggestion_note = models.TextField(null=True, blank=True)
    disclaimer = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    report_type=models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "test"

    def __str__(self):
        return self.test_name


    
class By_Parameter(models.Model):

    parameter=models.ForeignKey(Parameter, on_delete=models.CASCADE,related_name="by_parameter")
    sample=models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='by_parameter_sample')
    test=models.ForeignKey(Test,on_delete=models.CASCADE,related_name="by_parameter_test")
    
    class Meta:
        db_table = "By_Parameter"

    def __str__(self):
        return f"{self.test} - {self.report_type}"
    
class By_Template(models.Model):

    parameter=models.ForeignKey(Parameter, on_delete=models.CASCADE,related_name="by_template_parameter")
    sample=models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='by_template_sample')
    test=models.ForeignKey(Test,on_delete=models.CASCADE,related_name="by_template_test")
    
    class Meta:
        db_table = "By_Template"

    def __str__(self):
        return f"{self.test} - {self.report_type}"