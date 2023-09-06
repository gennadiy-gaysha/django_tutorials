from django.urls import path
from . import views

# namespaced - пространство имен
app_name = 'accounts'

# 'signup' - url name, which we use in our template
urlpatterns = [path('signup/', views.signup_view, name='signup')]