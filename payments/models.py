from django.db import models
from django.conf import settings
from courses.models import Course

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    ref_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {'پرداخت شد' if self.is_paid else 'در انتظار'}"
