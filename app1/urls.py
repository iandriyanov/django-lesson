#-*- coding: utf-8 -*-

############################################
#
# File Name : urls.py
#
# Purpose :
#
# Creation Date : 25-03-2014
#
# Last Modified : Wed 26 Mar 2014 07:58:40 PM MSK
#
# Created By : plushka
#
############################################


#from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'proj1.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^app1/basic/$', 'app1.views.basic'),
                       url(r'^app1/basic2/$', 'app1.views.basic2'),
                       url(r'^app1/test/$', 'app1.views.my_view'),
                       )
