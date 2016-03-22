from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import http
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template

from base import views as base_views

from . import model_forms as static_html_model_forms
from . import models as static_html_models
from . import conf as static_html_conf


class Create(base_views.BaseCreateView):
    editor = ''

    @method_decorator(login_required(login_url='log_in'))
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.has_perm("static_html_engine.add_statichtml"):
            return super(Create, self).dispatch(request, *args, **kwargs)
        else:
            return http.HttpResponseForbidden(get_template("403.html").render())

    def get_template_names(self):
        self.editor = self.request.GET.get('editor', '')
        if self.editor == 'pagedown':
            return ["static_html_engine/create-pagedown.html", ]
        elif self.editor == 'simple-markdown':
            return ["static_html_engine/create-simple-markdown-editor.html", ]
        elif self.editor == 'medium':
            return ["static_html_engine/create-medium.html", ]
        else:
            return ["static_html_engine/create.html", ]

    def get_form(self, form_class=None):
        self.editor = self.request.GET.get('editor', '')
        print self.editor
        if self.editor == 'pagedown' or self.editor == 'simple-markdown-editor':
            if self.request.POST:
                return static_html_model_forms.StaticHtmlMarkdown(self.request.POST)
            return static_html_model_forms.StaticHtmlMarkdown
        else:
            if self.request.POST:
                return static_html_model_forms.StaticHtml(self.request.POST)
            return static_html_model_forms.StaticHtml

    def form_valid(self, form):
        print "FORM VALID"
        static_page = form.save(commit=False)
        static_page.user = self.request.user
        static_page.save()
        return http.HttpResponseRedirect(reverse_lazy(
            static_page.url_name, kwargs={
                'slug': static_page.url
            }
        ))

    def form_invalid(self, form):
        print "Form INVLID"
        print form
        return self.render_to_response(self.get_context_data(form=form))


class List(base_views.BasePaginationListView):
    queryset = static_html_models.StaticHtml.objects.all()


class Detail(base_views.BaseDetailView):
    template_name = "static_html_engine/detail.html"
    model = static_html_models.StaticHtml

    def get_slug_field(self):
        return "url"


class Update(base_views.BaseUpdateView):
    editor = ''
    model = static_html_models.StaticHtml

    @method_decorator(login_required(login_url='log_in'))
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.has_perm("static_html_engine.update_statichtml"):
            return super(Update, self).dispatch(request, *args, **kwargs)
        else:
            return http.HttpResponseForbidden(get_template("403.html").render())

    def get_template_names(self):
        self.editor = self.request.GET.get('editor', '')
        if self.editor == 'pagedown':
            return ["static_html_engine/create-pagedown.html", ]
        elif self.editor == 'simple-markdown':
            return ["static_html_engine/create-simple-markdown-editor.html", ]
        elif self.editor == 'medium':
            return ["static_html_engine/create-medium.html", ]
        else:
            return ["static_html_engine/create.html", ]

    def get_form(self, form_class=None):
        self.editor = self.request.GET.get('editor', '')
        print self.editor
        print self.get_form_kwargs()['instance'].__dict__
        if self.editor == 'pagedown' or self.editor == 'simple-markdown':
            if self.request.POST:
                return static_html_model_forms.StaticHtmlMarkdown(self.request.POST)

            return static_html_model_forms.StaticHtmlMarkdown(self.get_form_kwargs()['instance'].__dict__)
        else:
            if self.request.POST:
                return static_html_model_forms.StaticHtml(self.request.POST)
            return static_html_model_forms.StaticHtml(self.get_form_kwargs()['instance'].__dict__)

    def form_valid(self, form):
        print "FORM VALID"
        static_page = form.save(commit=False)
        static_page.user = self.request.user
        static_page.save()
        return http.HttpResponseRedirect(reverse_lazy(
            static_page.url_name, kwargs={
                'pk': static_page.id
            }
        ))

    def form_invalid(self, form):
        print "Form INVLID"
        print form
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        print self.object
        return reverse_lazy(self.object.url_name, kwargs={
                'pk': self.object.id
            })

