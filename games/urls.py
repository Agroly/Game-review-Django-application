from django.urls import path


from . import views

urlpatterns = [
    path('create/game', views.GameCreateView.as_view(), name='game-create'),
    path('create/dev', views.DeveloperCreateView.as_view(), name='dev-create'),
]
