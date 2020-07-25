from django.conf.urls import url
from users.views import register,user_login,user_logout,get_all_users

urlpatterns = [
    url(r"^register/", register, name="register"),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^get_all_users/$', get_all_users, name='get_all_users'),
]
