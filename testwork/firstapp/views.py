from django.conf import settings  
from django.http import JsonResponse  
from django.shortcuts import render 
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from celery import current_app
from rest_framework.response import Response

from .tasks import demo
from rest_framework.views import APIView

class ArticleView(APIView):
	def get(self, request, task_id):
		task = current_app.AsyncResult(task_id)
		response_data = {'task_status': task.status,}
		if task.status == 'SUCCESS':
			response_data['results'] = task.get()
			return Response({"HTML-tags": response_data['results']})
		elif task.status == 'FAILURE':
			return Response('Task error')
		elif task.status == 'STARTED':
			return Response('THe task is not finishing')

	def post(self, request):
		url = request.data.get('URL')
		task = demo.delay(url)
		return Response(task.id)

def index(request):
	return render(request,"index.html")

