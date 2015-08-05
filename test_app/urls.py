from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic import TemplateView, RedirectView


class WrongVersionTestView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        request.lare.version = "0.0.0"
        return super(WrongVersionTestView, self).dispatch(request, *args, **kwargs)


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^old_version/$', WrongVersionTestView.as_view(), name='old_version'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^ignored-metatag/$', TemplateView.as_view(template_name='ignored_metatag.html'), name='ignored_metatag'),
    url(r'^no-matching-id/$', TemplateView.as_view(template_name='no_matching_id.html'), name='no_matching_id'),
    url(r'^no-lare-response/$', TemplateView.as_view(template_name='no_lare_response.html'), name='no_lare_response'),
    url(r'^lare-ready-lare-always/$', TemplateView.as_view(template_name='lare_ready_lare_always.html'), name='lare_ready_lare_always'),
    url(r'^lare-ready-lare-always/(?P<lare_state>(disabled))/$', TemplateView.as_view(template_name='lare_ready_lare_always.html'), name='lare_ready_lare_always'),
    url(r'^project/$', TemplateView.as_view(template_name='project.html'), name='project'),
    url(r'^project/blog/$', TemplateView.as_view(template_name='project_blog.html'), name='project_blog'),
    url(r'^project/gallery/$', TemplateView.as_view(template_name='project_gallery.html'), name='project_gallery'),
    url(r'^settings/$', TemplateView.as_view(template_name='settings.html'), name='settings'),

    # prevent travis 404 logs
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
)
