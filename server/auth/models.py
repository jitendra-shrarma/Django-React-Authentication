from django.db import models
from django.contrib.auth.models import User


class DailyEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    
    SENT = 'SENT'
    FAILED = 'FAILED'
    OPENED = 'OPENED'
    STATUS_CHOICES = [
        (SENT, 'sent'),
        (FAILED, 'failed')
        (OPENED, 'opened'),
    ]
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=SENT,
    )

    def __str__(self):
        return f'{self.email} ({self.user.username}): {self.status}'
