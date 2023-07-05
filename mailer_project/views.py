from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Email
from .serializers import EmailSerializer
import smtplib

class SendEmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.save()
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("your-email@gmail.com", "your-password")
                server.sendmail("your-email@gmail.com", email.to, f"Subject: {email.subject}\n\n{email.message}")
                server.quit()
                return Response({"message": "Email sent"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
