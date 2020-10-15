from django.urls import path
from . import views

urlpatterns = [
    path('search-user/', views.search_user, name="search_user"),
    path('registration/', views.UserRegisterView.as_view({'post':'create'}), name="register_user"),
    path('mark_spam/', views.mark_spam, name="mark_spam"),
]







