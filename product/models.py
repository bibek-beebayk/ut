from django.db import models


class Requirement(models.Model):
    product = models.CharField(max_length=255)
    email = models.EmailField()
    addressed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product
