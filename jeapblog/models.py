#coding:utf-8

from django.db import models
class Blog(models.Model):
	title       = models.CharField(max_length=140)
	content     = models.TextField()
	create_time = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title



	
