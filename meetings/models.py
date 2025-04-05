from django.db import models
from accounts.models import User
from courses.models import Course
import random
import string

class Meeting(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='meetings')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    link = models.URLField()  # لینک Jitsi / WebRTC / Google Meet
    participants = models.ManyToManyField(User, related_name='meetings', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"
    
# add a method to generate a unique meeting link
class Meeting(models.Model):
    ...
    link = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.link:
            random_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            clean_title = self.title.replace(' ', '')
            self.link = f"https://meet.jit.si/{clean_title}-{random_code}"
        super().save(*args, **kwargs)
