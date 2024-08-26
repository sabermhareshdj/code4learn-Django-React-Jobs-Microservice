import os , django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from faker import Faker
from django.utils import timezone
from django.utils.text import slugify
from job.models import Job, JOB_TYPE, EDUCATION_TYPE, EXPERIENCE_TYPE

fake = Faker()

def generate_dummy_jobs(num_jobs):
    for _ in range(num_jobs):
        title = fake.job()
        description = fake.paragraph(nb_sentences=10)
        job_type = random.choice([choice[0] for choice in JOB_TYPE])
        education = random.choice([choice[0] for choice in EDUCATION_TYPE])
        experience = random.choice([choice[0] for choice in EXPERIENCE_TYPE])
        salary = random.randint(30000, 100000)  # Assuming salary range
        position = fake.catch_phrase()
        due_date = fake.future_date(end_date='+30d')
        user_id = random.randint(1, 100)  # Assuming user IDs
        email = fake.email()
        company = fake.company()

        job = Job(
            title=title,
            description=description,
            job_type=job_type,
            education=education,
            experience=experience,
            salary=salary,
            position=position,
            due_date=due_date,
            user=user_id,
            email=email,
            company=company
        )
        job.save()


generate_dummy_jobs(10)