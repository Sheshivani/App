from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view({'post': 'create'}), name="register_user"),
    path('profile/<int:pk>/', views.ProfileView.as_view({'get': 'retrieve','patch': 'partial_update'}),
         name='user_profile'),
    path('article/', views.ArticleView.as_view({'post': 'create', 'get':'list'}),name='user_article'),
    path('buy/', views.BuyView.as_view({'post': 'create', 'get':'list'}),name='user_buy'),
    path('sell/', views.SellView.as_view({'post': 'create', 'get':'list'}),name='user_sell'),
]


