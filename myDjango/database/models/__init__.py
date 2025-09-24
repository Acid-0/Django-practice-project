from .user import User
from .role import Role

def get_all_fields(model, excluded_fields=None):
    if excluded_fields is None:
        excluded_fields = []
    return [
        field.name
        for field in model._meta.get_fields()
        if field.name not in excluded_fields and field.name != "_id"
    ]
