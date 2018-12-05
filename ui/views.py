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
        json_data = json.loads(request.body)
        try:
            visitor = SignatureVistor(name=json_data['name'],
                                      surname=json_data['surname'],
                                      email=json_data['email'])
            visitor.save()
        except Exception as e:
            return JsonResponse({'message': e.message}, status=400)
        return JsonResponse(json_data, status=200)
