from django.urls import path


from .views import *

urlpatterns = [
    path('', register, name='register'),
    path('register/', register, name='register'),
    path('registration_success/', registration_success, name='registration_success'),  # Add the actual view
   path('submit_ajax/', user_data_submit_ajax, name='user_data_submit_ajax'),
    path('admin-redirect/', admin_redirect_view, name='admin_redirect'),
]