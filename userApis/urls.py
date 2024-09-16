from django.urls import path
from . import views
urlpatterns= [
    path('users',views.User.as_view(),name="create"),
    path('users/<str:id>',views.UserWithId.as_view(),name="byId"),
    path('users/change-password/<str:id>',views.ChangeUserPassword.as_view(),name="changePassword"),
]