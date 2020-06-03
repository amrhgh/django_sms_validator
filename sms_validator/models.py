from django.db import models


class PhoneCode(models.Model):
    phone_number = models.CharField(unique=True)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(null=True, blank=True)
    expire_at = models.DateTimeField()

    class Meta:
        ordering = ('expire_at', )

    def __str__(self):
        return f'{self.phone_number} --- {self.expire_at}'
