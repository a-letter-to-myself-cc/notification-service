from django.urls import path, include

urlpatterns = [
    path("notify/", include("notify.urls")),  # ✅ 앱 URL 포함
]
