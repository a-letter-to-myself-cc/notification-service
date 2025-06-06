from django.urls import path, include
from notify.views import health_check  # ✅ 이거 맞아

urlpatterns = [
    path('notify/', include('notify.urls')),  # 앱 내부 URL 등록
    path('health/', health_check),            # ✅ 루트 health 경로 등록!
]