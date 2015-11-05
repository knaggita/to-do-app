# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
from .models import ActionPlan, Contact
from django.views.generic import View

class Task(View):
    template_name = 'tasks.html'
    def get(self, request):
         entries = ActionPlan.objects.all()
         t = loader.get_template(self.template_name)
         c = Context({
            'ActionPlan': entries
         })
         return HttpResponse(t.render(c))

class FollowUp(View):
    template_name = 'contacts.html'
    def get(self,request):
     entries = Contact.objects.all()
     t = loader.get_template(self.template_name)
     c = Context({
         'Contacts': entries
     })

     return HttpResponse(t.render(c))

class Index(View):
    template_name = 'index.html'
    def get(self, request):
     t = loader.get_template(self.template_name)
     return HttpResponse(t.render())


