from djongo import models

class Role(models.Model):
	_id= models.ObjectIdField()
	title=models.CharField(max_length=20)
	actions= models.JSONField(default=list, blank=True)
	action_type=models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "role"
