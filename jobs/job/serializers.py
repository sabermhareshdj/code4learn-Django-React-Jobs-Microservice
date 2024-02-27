from rest_framework import serializers
from .models import Job, JobApply

class jobSerializer(serializers.ModelSerializer):
  class Meta:
    model = Job
    fields = '__all__'

class jobApplySerializer(serializers.ModelSerializer):
  class Meta:
    model = JobApply
    fields = '__all__'
