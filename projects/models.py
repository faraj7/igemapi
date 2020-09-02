from django.db import models

class Project(models.Model):
	year = models.PositiveSmallIntegerField(default=0)
	team_name = models.CharField(max_length=200)
	wiki_link = models.URLField(max_length=200)
	location = models.CharField(max_length=200)
	region = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)
	section = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	track = models.CharField(max_length=200)
	abstract = models.TextField()
	parts_link = models.URLField(max_length=200)
	medal = models.CharField(max_length=200)
	nomination = models.CharField(max_length=200)
	award = models.CharField(max_length=200)
	class Meta:
		ordering = ('year','region','location','institution')

	def __str__(self):
		return self.team_name + str(self.year)