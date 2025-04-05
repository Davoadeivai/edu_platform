from rest_framework import viewsets, permissions
from .models import Meeting
from .serializers import MeetingSerializer
from notifications.utils import send_notification


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

# add a method to send notification when a meeting is created
# مثلا بعد از ایجاد جلسه:
send_notification(user, f"جلسه جدید '{meeting.title}' برای شما فعال شد!")
