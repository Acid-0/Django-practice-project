from database.models import User
from django.core.exceptions import ObjectDoesNotExist
import math

def post_user(name, email, age=None):
	user = User(_id=None, name=name, email=email, age=age)
	user.save()
	return None

def get_user(_id):
	user = User.objects.exclude(action_type=3).get(_id=_id)
	if user: return {"id": str(user._id), "name": user.name, "email": user.email, "age": user.age, "action_type":user.action_type} 
	else: return None

def get_all(page, limit):
    queryset = User.objects.exclude(action_type=3)
    total = queryset.count()

    offset = (page - 1) * limit
    users = queryset[offset:offset + limit]
    total_pages= math.ceil(total / limit)

    return {
        "total": total,
        "total_pages": total_pages,
        "result": [
            {
                "id": str(user._id),
                "name": user.name,
                "email": user.email,
                "age": user.age,
                "action_type": user.action_type,
            }
            for user in users
        ]
    }

def delete_user(_id):
    try:
        user = User.objects.get(pk=_id)
        user.delete()
        user.action_type = 3
        user.save()
        return True
    except ObjectDoesNotExist:
        return False
