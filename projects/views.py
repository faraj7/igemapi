from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from projects.models import Project
from projects.serializers import ProjectSerializer
from django_filters import rest_framework as filters

class ProjectFilter(filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'abstract': ['contains'],
            'institution': ['contains'],
            'year': ['exact'],
            'location': ['exact'],
            'region': ['exact'],
            'section': ['exact'],
            'track': ['exact'],
            'medal': ['exact'],
            'nomination': ['exact'],
            'award': ['exact'],
        }

class ProjectViewSet(viewsets.ModelViewSet):
    '''
    INSERT TEXT HERE
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProjectFilter
   # filterset_fields = ['year','location','region','institution','section','track','medal','nomination','award']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




'''
        projects_list = Project.objects.all()
        if request.GET.dict():
            if request.GET.get('year'):
                 projects_list = projects_list.filter(year=request.GET.get('year'))
            if request.GET.get('country'):
                projects_list = projects_list.filter(location__icontains = request.GET.get('country'))
            if request.GET.get('medal'):
                projects_list = projects_list.filter(medal__icontains = request.GET.get('medal'))
            if request.GET.get('keyword'):
                projects_list = projects_list.filter(abstract__icontains= request.GET.get('keyword'))
            if request.GET.get('institution'):
                projects_list = projects_list.filter(institution__icontains= request.GET.get('institution'))
            if request.GET.get('team_name'):
                projects_list = projects_list.filter(team_name__icontains= request.GET.get('team_name'))
            if request.GET.get('awards'):
                projects_list = projects_list.exclude(awards = "-")
            if request.GET.get('nominations'):
                projects_list = projects_list.exclude(nominations = "-")
            if request.GET.get('section'):
                projects_list = projects_list.filter(section__icontains= request.GET.get('section'))
            if request.GET.get('track'):
                projects_list = projects_list.filter(track__icontains= request.GET.get('track'))
    
    
    '''