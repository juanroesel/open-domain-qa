from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from bert_model.models import QAInput
from bert_model.serializers import CustomerSerializers
from bert_model.forms import InputForm 
from bert_model.apps import BertModelConfig
from django.shortcuts import render, redirect 
from django.contrib import messages 

# Sets up logging instance
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class InputView(viewsets.ModelViewSet): 
    queryset = QAInput.objects.all() 
    serializer_class = CustomerSerializers 


def home_view(request):
    if request.method=='POST':
        logging.info("Processing POST request")
        form = InputForm(request.POST or None)
        if form.is_valid():
            Question = form.cleaned_data['question']
            Context = form.cleaned_data['context']
            qa_inputs = {
                "question": Question,
                "context": Context
            }
            result = status(qa_inputs)
            logging.info("Request status: 200")
            return render(request, "templates/website/status.html", {"data": result})
        else:
            logging.error("Invalid request")
            
    form = InputForm()
    return render(request, "templates/website/home.html", {"form":form})


def status(qa_inputs):
    try:
        response = BertModelConfig.QA_BERT_model(
                    question=qa_inputs["question"],
                    context=qa_inputs["context"]
                )
        return response 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 