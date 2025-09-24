import math
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
    res = get_user(_id=_id),
    return Response({"result": res}, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_get_all(request):
    page = request.data.get("page")or 1
    limit = request.data.get("limit") or 10
    res = get_all(page=page,limit=limit)
    return Response({"total_pages":res["total_pages"],"page":page, "limit":limit, "result": res["result"]}, status=status.HTTP_200_OK)
