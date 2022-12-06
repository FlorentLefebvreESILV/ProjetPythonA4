from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visu', views.index0, name='index'),
    path('model', views.index1, name='index'),
    path('apply_visu', views.index2, name='index'),
    path('your-prediction', views.index3, name='index'),
]