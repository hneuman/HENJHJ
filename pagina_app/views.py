from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext


def main(request):
	print RequestContext(request)
	return render_to_response("main.html",context_instance=RequestContext(request))