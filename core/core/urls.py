from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from check_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-pdf/<int:check_pk>/', views.test_pdf, name='test_pdf'),
    path('<int:check_pk>/', views.check_generate, name='test-pdf'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
