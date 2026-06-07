from django.db import models


class OrderStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    PARTIAL = "PARTIAL", "Partial"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Cancelled"


class TestStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    COLLECTED = "COLLECTED", "Collected"
    SHIPPED = "SHIPPED", "Shipped"
    RECEIVED = "RECEIVED", "Received"
    RESAMPLING = "RESAMPLING", "Resampling"
    RESULT_PENDING = "RESULT_PENDING", "Result Pending"
    RESULT_ENTERED = "RESULT_ENTERED", "Result Entered"
    AUTHORIZED = "AUTHORIZED", "Authorized"
    COMPLETED = "COMPLETED", "Completed"
    REJECTED = "REJECTED", "Rejected"
    CANCELLED = "CANCELLED", "Cancelled"


class TestType(models.TextChoices):
    INHOUSE = "INHOUSE", "Inhouse"
    OUTSOURCE = "OUTSOURCE", "Outsource"


class PatientType(models.TextChoices):
    WALK_IN = "WALK_IN", "Walk-In"
    REGISTERED = "REGISTERED", "Registered"