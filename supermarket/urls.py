
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # DO NOT EDIT this file, go to market/urls.py
    path('market/',  include('market.urls')),
    path('accounts/', include('market.urls')),
    # path('accounts/',  include('market.urls')),
]
