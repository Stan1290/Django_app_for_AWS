from django.conf.urls import url
from . import views
from django.conf import settings

app_name = "acc_views"


urlpatterns = [

    url(r'^user/$', views.IndexView.as_view(), name='index'),

    url(r'^user/register/$', views.UserFormView.as_view(), name='register-user'),

    url(r'^user/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^user/add/$', views.AddUser.as_view(), name='user-add'),

    url(r'^user/(?P<pk>\d+)/delete/$', views.DeleteUser.as_view(), name='user-delete'),

    url(r'^user/(?P<pk>\d+)/edit/$', views.EditUser.as_view(), name='user-edit'),







    #add an account to a user: acc_views/<users_id>/add_account
    #url(r'^(?P<users_id>[0-9]+)$/add_account', views.add_account, name='add_account'),
]
