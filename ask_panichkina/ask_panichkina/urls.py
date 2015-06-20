from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask_panichkina.views import index, login, signup, ask_question

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_panichkina.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^helloworld/', 'ask_panichkina.views.helloworld', name='helloworld'),
    url(r'^$', index, name='index'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^ask_question/$', ask_question, name='ask_question'),
    url(r'^question/(\d+)/$', 'ask_panuchkina.views.question', name='question'),
)