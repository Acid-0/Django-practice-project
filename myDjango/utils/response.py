from rest_framework.response import Response
from rest_framework import status
import math

def success_response(data=None, message="success", code=status.HTTP_200_OK, page=0, limit=0, total_records=0):
    return Response(
        {
            "success": True,
            "message": message,
            "page": page,
            "limit": limit,
            "total_pages": math.ceil(total_records / limit) if limit>0 else 0,
            "data": data
        },
        status=code
    )

def error_response(message="something went wrong", code=status.HTTP_400_BAD_REQUEST, errors=None, data=None):
    return Response(
        {
            "success": False,
            "message": message,
            "errors": errors,
            "data": data
        },
        status=code
    )
