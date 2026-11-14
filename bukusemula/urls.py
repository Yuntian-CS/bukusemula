from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from main.views import ChangeLanguageView, IndexPageView
# myproject/urls.py (your main root urls.py)
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings

def firebase_sw(request):
    sw_path = settings.CONTENT_DIR / 'assets' / 'js' / 'firebase-messaging-sw.js'
    return HttpResponse(sw_path.read_text(), content_type='application/javascript')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexPageView.as_view(), name="index"),
    path("i18n/", include("django.conf.urls.i18n")),
    path("language/", ChangeLanguageView.as_view(), name="change_language"),
    path("accounts/", include("accounts.urls")),
    path('firebase-messaging-sw.js', firebase_sw),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
