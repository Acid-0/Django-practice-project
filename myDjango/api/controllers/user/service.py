from database.models import User
from django.core.exceptions import ObjectDoesNotExist


def post_user(name, email, age=None):
	user = User(_id=None, name=name, email=email, age=age)
	user.save()
	return None

def get_user(_id):
	user = User.objects.get(_id=_id)
	if user: return {"id": str(user._id), "name": user.name, "email": user.email, "age": user.age} 
	else: return None

def get_all():
    users = User.objects.all()
    return [{"id": str(user._id), "name": user.name, "email": user.email, "age": user.age} for user in users]

def delete_user(_id):
    try:
        user = User.objects.get(pk=_id)
        user.delete()
        return True
    except ObjectDoesNotExist:
        return False
