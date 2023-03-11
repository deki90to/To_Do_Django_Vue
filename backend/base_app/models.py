from django.db import models



class Todo(models.Model):
	task = models.CharField(max_length=200, blank=False, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'Task: {self.task}, created: {self.created_at}'

	class Meta:
		ordering=['-created_at']