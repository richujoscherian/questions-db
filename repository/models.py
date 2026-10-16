from django.db import models

# Create your models here.
class QuestionsDb(models.Model):
    title=models.CharField(max_length=200)

    LANGUAGE_CHOICES=(
        ("python","Python"),
        ("javascript","Javascript"),
        ("c","C"),
        ("c++","C++"),
    )

    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="python")

    DIFFICULTY_CHOICES=(
        ("easy","easy"),
        ("medium","medium"),
        ("hard","hard"),
    )
    difficulty=models.CharField(max_length=100,choices=DIFFICULTY_CHOICES,default="easy")

    topic=models.CharField(max_length=100)
    notes=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    sample_input=models.TextField()
    sample_output=models.TextField()
    is_active=models.BooleanField(default=True)
    score=models.IntegerField()
