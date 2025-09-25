from rest_framework.decorators import api_view
from utils.response import success_response, error_response
from utils.enums import ResponseMessages, ResponseCodes
from utils.customError import CustomError
from .role_service import post as postService, get as getService, get_all as getAllService, deleteById as deleteByIdService

@api_view(['POST'])
def post(request):
    try:
          title = request.data.get("title")
          actions = request.data.get("actions") or []
          res = postService(title=title, actions=actions )
          return success_response(data=res, message=ResponseMessages.SAVE_SUCCESS.value)
    except CustomError as ce:
        return error_response(message=ce.message, code=ce.status_code, data=ce.data)
    except Exception as err:
          return error_response(message=ResponseMessages.EXCEPTION.value, code=ResponseCodes.exception.value, errors=err )
          


@api_view(['GET'])
def get(request):
    try:
          _id = request.query_params.get("_id")
          res = getService(_id=_id)
          return success_response(data=res, message=ResponseMessages.DATA_FOUND.value)
    except CustomError as ce:
        return error_response(message=ce.message, code=ce.status_code, data=ce.data)
    except Exception as err:
        return error_response(message=ResponseMessages.EXCEPTION.value, code=ResponseCodes.exception.value, errors=err )


@api_view(['GET'])
def get_all(request):
    try:
        page = request.data.get("page")or 1
        limit = request.data.get("limit") or 10
        res = getAllService(page=page,limit=limit)
        return success_response(data=res["result"], message=ResponseMessages.DATA_FOUND.value, page=page,limit=limit, total_records=res["total"] )
    except CustomError as ce:
        return error_response(message=ce.message, code=ce.status_code, data=ce.data)
    except Exception as err:
        return error_response(message=ResponseMessages.EXCEPTION.value, code=ResponseCodes.exception.value, errors=err )

@api_view(['POST'])
def deleteById(request):
    try:
        _id = request.data.get("_id")
        res = deleteByIdService(_id=_id)
        return success_response(data=res, message=ResponseMessages.DELETE_SUCCESS.value)
    except CustomError as ce:
        return error_response(message=ce.message, code=ce.status_code, data=ce.data)
    except Exception as err:
        return error_response(message=ResponseMessages.EXCEPTION.value, code=ResponseCodes.exception.value, errors=err )
