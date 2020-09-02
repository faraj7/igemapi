from django.contrib.auth.models import User
from rest_framework import serializers

from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('year', 'team_name', 'wiki_link', 'location', 'region', 'institution',
                  'section', 'title', 'track', 'abstract', 'parts_link', 'medal', 'nomination', 'award')