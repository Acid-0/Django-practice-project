from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .service import post_user, get_user, get_all

@api_view(['POST'])
def view_post(request):
	name = request.data.get("name")
	email = request.data.get("email")
	age = request.data.get("age")
	result = post_user(name=name, email=email,age=age )
	return Response({"result":result}, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_get(request):
    _id = request.query_params.get("_id")  # safer for GET requests
    result = get_user(_id=_id)
    return Response({"result": result}, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_get_all(request):
    result = get_all()
    return Response({"result": result}, status=status.HTTP_200_OK)
