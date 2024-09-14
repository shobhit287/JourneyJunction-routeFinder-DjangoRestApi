from django.urls import path
from . import views
urlpatterns= [
    path('',views.User.as_view(),name="create"),
    path('/<str:id>',views.User.as_view(),name="byId"),
    path('/change-password/<str:id>',views.ChangeUserPassword.as_view(),name="getbyId"),
]