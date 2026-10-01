from django.urls import path

from . import views


urlpatterns=[


path('',views.home,name='home'),

path('register/',
views.register,
name='register'),


path('login/',
views.user_login,
name='login'),


path('logout/',
views.user_logout,
name='logout'),


path('submit/',
views.submit_request,
name='submit'),


path('requests/',
views.my_requests,
name='my_requests'),


path('update/<int:id>/',
views.update_request,
name='update'),


path('delete/<int:id>/',
views.delete_request,
name='delete'),


path('dashboard/',
views.admin_dashboard,
name='dashboard'),


]