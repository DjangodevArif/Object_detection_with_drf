from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def index(request):
    return Response("Hello, world. You're at the main page")
