from sodp.forms import DemoForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import DemoForm
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

class DemoFormView(FormView):
    template_name = 'pages/demo.html'
    form_class = DemoForm
    success_url = '/thanks/'

    def form_valid(self, form):
        print(self.email)
        message = get_template("emails/demoRequest.html").render({
            'email': form.cleaned_data.get('email')
        })
        mail = EmailMessage(
            "Demo Request",
            message,
            form.cleaned_data.get('email'),
           to=['settings.EMAIL_FROM']
        )
        mail.content_subtype = "html"
        mail.send()
        return super(DemoFormView,self).form_valid(form)