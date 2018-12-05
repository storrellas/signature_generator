from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from .models import SignatureVistor


class SignatureGeneratorView(View):
    def get(self, request):
        context = {}
        return render(request, 'signature.html', context)


    def post(self, request):
        received_json_data=json.loads(request.body)
        print(received_json_data['name'])
        print(received_json_data['surname'])
        print(received_json_data['email'])



        #context = {}
        #return render(request, 'signature.html', context)
        return JsonResponse({'status':'false','message':'stored'}, status=200)
