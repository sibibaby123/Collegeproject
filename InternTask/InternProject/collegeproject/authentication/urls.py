from django.urls import path
from . import views

app_name= 'authentication'

urlpatterns=[
    path('',views.allCourse,name="allCourse"),
    path('signin',views.signin,name="signin"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('dataform',views.dataform,name="dataform"),
    path('department/<slug>',views.department,name="department"),
    path('purpose/<slug>',views.purpose,name="purpose"),
    path('item',views.item,name="item"),
]

