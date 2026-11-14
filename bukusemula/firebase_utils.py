import firebase_admin
from firebase_admin import credentials, messaging
from sports.settings import cred_path
import os

cred_path = os.path.join(BASE_DIR / 'secrets/bukusemula-firebase-adminsdk-fbsvc-d33b3940a1.json')
# Initialize Firebase app only once
firebase_app = None

def initialize_firebase():
    global firebase_app
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_app = firebase_admin.initialize_app(cred)

def send_push_notification(token, title, body, data=None):
    """
    Send push notification to a device via FCM.
    """
    initialize_firebase()

    message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
                ),
            token=token,
            data=data or {},
            )

    response = messaging.send(message)
    return response

class PushNotification(APIView):
    serializer_class = FcmTokenSerializer()


    def post(self, request):
        serializer = FcmTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return MyResponse.failure(message="Invalid input", errors=serializer.errors)

        token = serializer.validated_data["fcm_token"]

        send_push_notification(
                token=token,
                title="Welcome!",
                body="Thanks for joining my channel",
                data={"click_action": "FLUTTER_NOTIFICATION_CLICK"}
                )
        return MyResponse.success(message="Notification sent successfully")
