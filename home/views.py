from django.shortcuts import render
from django.views.generic import View
from django.views import View
from authentication.models import User


# Create your views here.
class DashView(View):
    def render(self, request):
        context = {}
        return render(request, "pages/dash.html", context)

    def post(self, request):
        pass

    def get(self, request):
        return self.render(request)
