from django.db import models


from restapi.models.result_entry_model import ResultEntry

class Authorization(models.Model):

    result_entry = models.ForeignKey(
        ResultEntry,
        on_delete=models.CASCADE,
        related_name="authorizations",
        null=True,
        blank=True
    )

    

    order_date = models.DateField()
    order_time = models.TimeField()

    patient_name = models.CharField(max_length=200)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=20)

    patient_code = models.CharField(max_length=100)
    patient_type = models.CharField(max_length=100)

    doctor_name = models.CharField(max_length=200)
    bill_no = models.CharField(max_length=100)

    no_of_orders = models.IntegerField(default=0)

    test_name = models.CharField(max_length=200)

    result_status = models.CharField(
        max_length=50,
        default="Completed"
    )

    authorization_status = models.CharField(
        max_length=50,
        default="Pending"
    )

    authorized_by = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    authorized_date = models.DateTimeField(
        null=True,
        blank=True
    )

    remark = models.TextField(
        null=True,
        blank=True
    )

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.patient_name
