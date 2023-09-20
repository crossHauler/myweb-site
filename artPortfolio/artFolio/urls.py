from django.urls import path
from . import views

urlpatterns = [
	path('simple/',views.simple_view),
	path('example/', views.example_view, name='example'),
	path('', views.index, name='index'),
	path('index/', views.index, name='index'),
	path("<int:artwork_id>/", views.detail, name="detail"),
]