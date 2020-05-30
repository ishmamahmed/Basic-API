# from django.conf.urls import url, include
from django.urls import path, include

from .views import myAdminRudView
app_name = 'postings'
urlpatterns = [
    path('<pk>/', myAdminRudView.as_view(), name='post-rud')
]