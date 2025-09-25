from enum import Enum

class ErrorCode(Enum):
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    EXCEPTION = 500
    NOT_VERIFIED = 422
    PAYMENT_REQUIRED = 402
    LIMIT_EXCEED = 429
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    INVALID_DATA = 422


class CustomError(Exception):
    def __init__(self, message: str, status_code: int, data=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.data = data or {}

    def to_dict(self):
        """Convert error details into a dictionary (useful for responses)."""
        return {
            "message": self.message,
            "statusCode": self.status_code,
            "data": self.data,
        }


class Errors:
    # client errors
    BAD_REQUEST = CustomError("Bad request: Invalid argument/invalid request payload", ErrorCode.BAD_REQUEST.value)
    NOT_FOUND = CustomError("Id/record not found", ErrorCode.NOT_FOUND.value)
    CONFLICT = CustomError("Record Already Exist", ErrorCode.CONFLICT.value)
    ID_REQUIRED = CustomError("A valid Id required", ErrorCode.BAD_REQUEST.value)
    EXCEPTION = CustomError("Exception occurred", ErrorCode.EXCEPTION.value)
    UNAUTHORIZED = CustomError("Invalid credentials", ErrorCode.UNAUTHORIZED.value)
    NOT_VERIFIED = CustomError("Validation failed! user email/profile not verified or missing", ErrorCode.NOT_VERIFIED.value,)
    PAYMENT_REQUIRED = CustomError("Payment required!", ErrorCode.PAYMENT_REQUIRED.value)
    FORBIDDEN = CustomError("Access restricted! not authorized", ErrorCode.FORBIDDEN.value)
    LIMIT_EXCEED = CustomError("Available limit has exceeded", ErrorCode.LIMIT_EXCEED.value)
    LOCKED = CustomError("Resource locked", ErrorCode.LOCKED.value)
    FAILED_DEPENDENCY = CustomError("Failed dependency/Incomplete_profile", ErrorCode.FAILED_DEPENDENCY.value)

    # server errors
    INTERNAL_SERVER_ERROR = CustomError("Internal Server Error", ErrorCode.INTERNAL_SERVER_ERROR.value)
    NOT_IMPLEMENTED = CustomError("Feature not implemented", ErrorCode.NOT_IMPLEMENTED.value)
    SERVICE_UNAVAILABLE = CustomError("Service temporarily unavailable", ErrorCode.SERVICE_UNAVAILABLE.value)
    GATEWAY_TIMEOUT = CustomError("Upstream service timeout", ErrorCode.GATEWAY_TIMEOUT.value)

    # specified errors
    class User:
        NOT_FOUND = CustomError("User not exist", ErrorCode.NOT_FOUND.value)
        ID_NOT_FOUND = CustomError("A valid Id User required", ErrorCode.NOT_FOUND.value)
        INVALID_CODE = CustomError("Invalid verification code", ErrorCode.INVALID_DATA.value)
        INVALID_DATA_MATCH = CustomError("Given data/information is not valid", ErrorCode.NOT_VERIFIED.value)


def create_data_custom_error(msg: str, status_code: int, data=None):
    """Factory to create custom errors with dynamic message/data"""
    return CustomError(msg, status_code, data or {})
