from django.urls import path
from . import views

urlpatterns = [
    #notify.views.test_notification_api
    path("send/", views.test_notification_api, name="send_notification"), #/api/notify/send/
    # POST로 알림 요청 받는 엔드포인트
    path("email/", views.email_notification_api), #/api/notify/email/ 
]
