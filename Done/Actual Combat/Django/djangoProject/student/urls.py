#conding = utf-8


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index_view),
    url(r'^logon/$',views.logon_view),
    url(r'^register/$',views.register_view),
    url(r'eds/',views.edslogon_view),
    url(r'show/',views.show_view),
    url(r'text/',views.ybjs_test)
]