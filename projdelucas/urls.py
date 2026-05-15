from django.contrib import admin
from django.urls import path
from financeiro.views import home, login_view, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('login/', login_view, name='login'),

    path('dashboard/', dashboard, name='dashboard'),
]