from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import jobSerializer , jobApplySerializer
from .models import Job , JobApply
from .filters import JobFilter
from .pagination import JobsPagination

class JobListCreateAPI(generics.ListCreateAPIView):
  queryset = Job.objects.all()
  serializer_class = jobSerializer
  filter_backends = [DjangoFilterBackend,filters.SearchFilter]
  filterset_class = JobFilter
  pagination_class = JobsPagination


class JobDetailUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
  queryset = Job.objects.all()
  serializer_class = jobSerializer