from django.db import models
from django.utils import timezone



JOB_TYPE = (
  ('Internship','Internship'),
  ('PartTime','PartTime'),
  ('FullTime','FullTime'),
  ('Contract','Contract'),
)

EDUCATION_TYPE = (
  ('PHD','PHD'),
  ('Master','Master'),
  ('Bachelor','Bachelor'),
)

EXPERIENCE_TYPE = (
  ('NoExperience','NoExperience'),
  ('Junior','Junior'),
  ('MidLevel','MidLevel'),
  ('MidSenior','MidSenior'),
)

class Job(models.Model):
  title = models.CharField(max_length=150)
  description = models.TextField(max_length=20000)
  job_type = models.CharField(max_length=15,choices=JOB_TYPE)
  education = models.CharField(max_length=15,choices=EDUCATION_TYPE)
  experience = models.CharField(max_length=15,choices=EXPERIENCE_TYPE)
  salary = models.IntegerField()
  position = models.CharField(max_length=100)
  due_date = models.DateField()
  created_at = models.DateTimeField(default=timezone.now)

  user = models.IntegerField()
  email = models.EmailField()
  company = models.CharField(max_length=30)

  def __str__(self):
    return self.title


class JobApply(models.Model):
  user = models.IntegerField()
  job = models.ForeignKey(Job,related_name='applied_job',on_delete=models.CASCADE)
  resume = models.CharField(max_length=200)
  cover_letter = models.TextField(max_length=500)
  applied_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return str(self.job)


