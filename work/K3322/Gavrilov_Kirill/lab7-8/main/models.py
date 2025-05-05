from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(4)], null=True, blank=True)
    service = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


