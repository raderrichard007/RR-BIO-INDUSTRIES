"""
URL configuration for rrbioindustries project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from Services import views


home_patterns = [
    path('', views.home, name='home'),
    path('stocklist/', views.stock_list, name='stock_list'),
    path('stock/', views.stock, name='stock'),
    path('credit/', views.credit_note, name='credit_note'),
    path('invoice/', views.invoice, name='invoice'),
    path('attendance_form/', views.attendance_form, name='attendance_form'),
    path('add-member/', views.add_member, name='add_member'),
    path('save_member/',views.save_member, name='save_member'),
    path('daily_production/',views.daily_production, name='daily_production'),
    path('raw/',views.raw, name='raw'),
    path('salary_page/', views.salary_page, name='salary_page')
    # path('save_attendance/',views.save_attendance, name='save_attendance'),
    # path('get_members/', views.get_members, name='get_members')

]

urlpatterns = [
    path("", views.loginUser, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("home/", include(home_patterns)),
    path("admin/", admin.site.urls, name="admin"),
]


admin.site.site_header = "Admin Panal"
admin.site.site_title = "Admin"
admin.site.index_title = "RR Bio Industries"