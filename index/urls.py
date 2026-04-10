from django.urls import path
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.home, name='home'),
    path('fio', views.fio, name='fio'),
    path('profile/<int:id>', views.profile, name="profile"),
    path('isiform', views.isiform, name='isiform'),
    path('isiform2', views.isiForm2, name='isiform2'),
    path('isiform/submit', views.isiformsubmit, name='isiformsubmit')
    
]