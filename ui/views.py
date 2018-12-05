from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


class SignatureGeneratorView(View):
    def get(self, request):
        context = {}
        return render(request, 'signature.html', context)


    def post(self, request):
        #context = {}
        #return render(request, 'signature.html', context)
        return JsonResponse({'status':'false','message':'stored'}, status=200)
