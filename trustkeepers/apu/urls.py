from django.urls import path
from . import views
urlpatterns=[
    path('contact/',views.ContactView.as_view()),
    path('bookmeeting/',views.BookMeetingView.as_view())
]