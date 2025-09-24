from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .role_service import post as postService, get as getService, get_all as getAllService, deleteById as deleteByIdService

@api_view(['POST'])
def post(request):
	title = request.data.get("title")
	actions = request.data.get("actions") or []
	result = postService(title=title, actions=actions )
	return Response({"result":result}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get(request):
    _id = request.query_params.get("_id")  # safer for GET requests
    res = getService(_id=_id),
    return Response({"result": res}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all(request):
    page = request.data.get("page")or 1
    limit = request.data.get("limit") or 10
    res = getAllService(page=page,limit=limit)
    return Response({"total_pages":res["total_pages"],"page":page, "limit":limit, "result": res["result"]}, status=status.HTTP_200_OK)

@api_view(['POST'])
def deleteById(request):
    _id = request.data.get("_id")
    res = deleteByIdService(_id=_id),
    return Response({"result": res}, status=status.HTTP_200_OK)
