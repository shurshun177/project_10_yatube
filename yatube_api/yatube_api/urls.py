from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Надо исправить: Подключаем приложение api через api/, а не через api/v1/,
    # так как внутри приложения api у нас может быть несколько версий.
    # Студентам надо рассказать, зачем нужно версионирование.
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
