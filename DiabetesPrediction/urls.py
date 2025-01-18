from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home, name='home'),
    path('about/', view.about, name='about'),
    path('predict/', view.predict, name='predict'),
    path('predict/result', view.result, name='result')
]
