from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeapblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^home$', 'jeapblog.views.home'),
    url(r'^test/(\w+)$', 'jeapblog.views.test'),
    url(r'^test1/\w+$', 'jeapblog.views.test1'),
	#CURD
    url(r'^blog_create$', 'jeapblog.views.blog_create'),
    url(r'^list$', 'jeapblog.views.blog_list'),
    url(r'^blog_update/(\d+)$', 'jeapblog.views.blog_update'),
    url(r'^delete/(\d+)$', 'jeapblog.views.blog_delete'),
    url(r'^blog_create_form$', 'jeapblog.views.blog_create_form'),
    url(r'^blog_update_save/(\d+)$', 'jeapblog.views.blog_update_save'),
)
