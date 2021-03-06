"""deposit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
admin.autodiscover()
import deposits.views

from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', deposits.views.IndexView.as_view(),name='main'),
    #path('add_user1', users_app.views.AddUserView1.as_view()),
    path('deposit/new', deposits.views.AddDepositView.as_view()),
    path('deposit/<int:pk>', deposits.views.GetDepositView.as_view()),
    #path('edit_user/<int:pk>', users_app.views.EditUserView.as_view()),
    #path('delete_user/<int:pk>', users_app.views.DeleteUserView.as_view()),
    #path('add_user', users_app.views.add_user)
]
