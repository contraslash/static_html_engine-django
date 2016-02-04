from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import http
from django.core.urlresolvers import reverse_lazy

from base import views as base_views

from . import model_forms as static_html_model_forms
from . import models as static_html_models
from . import conf as static_html_conf


class Create(base_views.BaseCreateView):
    template_name = "static_html_engine/create.html"
    form_class = static_html_model_forms.StaticHtml

    @method_decorator(login_required(login_url='log_in'))
    def dispatch(self, request, *args, **kwargs):
        return super(Create, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        static_page = form.save(commit=False)
        static_page.user = self.request.user
        static_page.save()
        return http.HttpResponseRedirect(reverse_lazy(
            static_page.url_name, kwargs={
                'pk': static_page.id
            }
        ))


class List(base_views.BasePaginationListView):
    queryset = static_html_models.StaticHtml.objects.all()


class Detail(base_views.BaseDetailView):
    template_name = "static_html_engine/detail.html"
    model = static_html_models.StaticHtml


class Update(base_views.BaseUpdateView):
    template_name = "static_html_engine/update.html"
    form_class = static_html_model_forms.StaticHtml
    model = static_html_models.StaticHtml
    def get_success_url(self):
        print self.object
        return reverse_lazy(self.object.url_name, kwargs={
                'pk': self.object.id
            })

