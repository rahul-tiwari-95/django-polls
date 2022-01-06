import datetime

from django.db import models
from django.utils import timezone

#we will create models here

#Question model has Question & Pub_Date
#Choice model has question (Foreign_Key), choice_text, votes  

class Question(models.Model):
    question_text = models.CharField(max_length=350)
    pub_date = models.DateTimeField('date published')

    #we declared this to convert everything into a readable format  
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_test = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self) :
        return self.choice_test





