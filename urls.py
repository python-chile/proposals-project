from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import social_django.urls

from src.accounts import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.proposals.urls')),
    path('accounts/', include(urls)),
    path('accounts/', include(social_django.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)