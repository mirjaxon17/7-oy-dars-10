from django.shortcuts import render
from django.views import View


class HomePageView(View):
    def get(self, request):
        search = request.GET.get('search')
        return render(request, "index.html")
