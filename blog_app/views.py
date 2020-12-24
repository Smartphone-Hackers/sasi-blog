from django.shortcuts import render
from django.views import View

# Create your views here.
class Blog(View):
    template_name = 'blog-index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class Home(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class Oracle(View):
    template_name = 'oracle.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class BSelectstmt(View):
    template_name='ora_sql_basicselectstmt.html'
    def get(self,request):
        return render(request,template_name=self.template_name)

class Retrieving_Data(View):
    template_name='ora_sql_retrievingdata.html'
    def get(self,request):
        return render(request,template_name=self.template_name)