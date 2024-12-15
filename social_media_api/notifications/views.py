from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, is_read=False)
        notifications_data = [{"actor": notif.actor.username, "verb": notif.verb, "timestamp": notif.timestamp} for notif in notifications]
        return Response({"notifications": notifications_data}, status=200)
