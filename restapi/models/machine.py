from django.db import models

class Machine(models.Model):
    machine_code = models.CharField(max_length=50, unique=True)
    machine_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.machine_name
    
    class meta:
        db_table = "Machine"

class Machine_Parameters(models.Model):
    machine = models.ForeignKey("Machine", on_delete=models.CASCADE, related_name="machine_parameters")
    machine_parameter_code = models.CharField(max_length=50,)
    machine_parameter_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.machine_parameter_name
    
    class Meta:
        db_table = "Machine_Parameter"