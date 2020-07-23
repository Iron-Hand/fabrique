from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class QuestionType(models.Model):
    name = models.TextField(max_length=20)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='q', on_delete=models.CASCADE)
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    text = models.TextField()

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    

class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.TextField()

    class Meta:
        unique_together = (('user', 'poll', 'question'))