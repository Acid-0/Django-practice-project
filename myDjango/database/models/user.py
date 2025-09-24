from djongo import models
from bson import ObjectId

class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # email = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(default=0)

    class Meta:
        db_table = "user"  # custom collection name
