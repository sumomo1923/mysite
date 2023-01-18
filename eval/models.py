from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Eval_item_word(models.Model):
    word_sentence = models.CharField(max_length=200)
    eval_component = models.CharField(max_length=200)
    eval_word = models.CharField(max_length=200)

    def __str__(self):
        return self.eval_word

class Eval_item_sentence(models.Model):
    sentence_text = models.CharField(max_length=200)

    def __str__(self):
        return self.sentence_text

