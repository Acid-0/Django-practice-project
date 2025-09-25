from database.models import Role
from django.core.exceptions import ObjectDoesNotExist
from bson import ObjectId
from utils.customError import Errors

def post(title, actions):
	role = Role(title=title, actions=actions)
	role.save()
	return str(role._id)

def get(_id):
    if not _id:
     raise Errors.BAD_REQUEST
    
    role = Role.objects.exclude(action_type=3).filter(_id=ObjectId(_id)).first()
    
    if role: return {"id": str(role._id), "title": role.title, "actions": role.actions, "action_type":role.action_type} 
    else: raise Errors.NOT_FOUND

def get_all(page, limit):
    queryset = Role.objects.exclude(action_type=3)
    total = queryset.count()

    offset = (page - 1) * limit
    roles = queryset[offset:offset + limit]

    return {
        "total": total,
        "result": [
            {
                "id": str(role._id),
                "title": role.title,
                "actions": role.actions,
				"created_at": role.created_at,
				"updated_at": role.updated_at,
            }
            for role in roles
        ]
    }


def deleteById(_id):
    try:
        role = Role.objects.get(pk=ObjectId(_id))
        # role.delete()
        role.action_type = 3
        role.save()
        return True
    except ObjectDoesNotExist:
        return False
