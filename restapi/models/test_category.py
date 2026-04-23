from django.db import models


class Category(models.Model):

    test=models.ForeignKey('Test', on_delete=models.CASCADE, related_name="category_tests")
    category_code = models.CharField(max_length=50, unique=True)
    category_name = models.CharField(max_length=100)
    status= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name