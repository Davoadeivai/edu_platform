from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Payment
from courses.models import Course
from payments.models import Payment
import uuid

class StartPaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=404)

        payment = Payment.objects.create(
            user=request.user,
            course=course,
            amount=course.price
        )
        
        # Mock: پرداخت تستی (درگاه واقعی در مرحله بعد)
        payment.is_paid = True
        payment.ref_id = str(uuid.uuid4())
        payment.save()

        return Response({'message': 'پرداخت موفق', 'ref_id': payment.ref_id})

# add new 

class MyCoursesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        paid_courses = Course.objects.filter(payment__user=request.user, payment__is_paid=True)
        data = [{'id': c.id, 'title': c.title} for c in paid_courses]
        return Response(data)
