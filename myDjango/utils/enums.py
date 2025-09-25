from enum import Enum

class ResponseMessages(Enum):
	SAVE_SUCCESS="Data saved successfully"
	UPDATE_SUCCESS="Data updated successfully"
	DELETE_SUCCESS="Data delete successfull"
	DATA_FOUND="Data found successfull"
	EXCEPTION="Some exception occur"

class ResponseCodes(Enum):
	#Success codes
	success = 200, #OK(standard successful HTTP request)
	created = 201, #Resource created successfully
	accepted = 202, #Request accepted for processing
	updated = 204, #Success but no content to return ('updated')

	#Client error codes
	bad_request = 400, #General client error('failed')
	unauthorized = 401, #Authentication needed('token_required' and 'token_invalid')
	payment_required = 402,
	forbidden = 403, #Authenticated but not authorized('access_restricted')
	not_found = 404, #Resource not found('not_exist')
	conflict = 409, #Resource conflict('exist')
	not_verified = 422, #Validation errors (can't proccess request - user email/profile not verified or missing)
	limit_exceed = 429, #Rate limiting('limit_exceed')
	locked = 423, #Resource locked
	failed_dependency = 424, #Failed dependency('incomplete_profile')

	#Server error codes
	internal_server_error = 500,
	not_implemented = 501, #Feature not implemented
	service_unavailable = 503, #Service temporarily unavailable
	gateway_timeout = 504, #Upstream service timeout

	#Custom logic codes
	exception = 500,
	invalid_data = 400,
	duplicate = 409, #Duplicate data