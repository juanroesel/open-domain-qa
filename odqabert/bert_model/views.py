from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import BertModelConfig


class test_model(APIView):
    """Testing view to test API requests calls to the QA BERT model."""
    def get(self, request):
        if request.method == 'GET':
            # question is the query we want to get the prediction for
            question = request.GET.get('question') + "?"
            context = "This is a dummy context to help test the API call"
            # predict method used to get the prediction
            print(question)
            response = BertModelConfig.QA_BERT_model(
                    question=question,
                    context=context
                )
            # returning JSON response
            print(response)
            return JsonResponse(response, safe=False)
