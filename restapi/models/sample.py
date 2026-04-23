from django.db import models

class Sample(models.Model):
    sample_code= models.CharField(max_length=50, unique=True)
    sample_name= models.CharField(max_length= 100)
    status= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sample_name
    class meta:
        db_table = "sample"
