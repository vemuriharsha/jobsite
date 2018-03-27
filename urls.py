import sendmail as sendmail
from django.conf.urls import include, url
from django.conf import settings
from django.views.generic.base import TemplateView
#from views import *
from jobs import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^main/$',views.main),
    url(r'^homepage/$',views.home_page),
    url(r'^search/$',views.search),
    url(r'^search1/$',views.search1),
    url(r'^apply/$',views.apply),
    url(r'^store/$',views.store),

    url(r'^time/$',views.current_datetime),
    #url(r'^$',views.home,name="home"),
    #url(r'^registration/$', views.register),
    #url(r'^register1/$', views.register1),
    url(r'^index/$', views.index),
    url(r'^success', views.success, name='success'),
    url(r'^home/', views.home),
    url(r'^$', views.login),
    url(r'^home1/$', views.home1),
    url(r'^home2/$', views.home2),
    url(r'^complete/$', views.complete),
    url(r'^logout/$', views.logout),
    url('',include('social_django.urls',namespace='social')),
    #url(r'', include('social_auth.urls')),

    #url(r'^email/send/$', sendmail),
    #url(r'^email/thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
    #url(r'^email/$', TemplateView.as_view(template_name='email.html'), name='email'),
    url(r'^disconnect', views.disconnect),
    url(r'^join', views.join),
    url(r'^google',views.google),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

