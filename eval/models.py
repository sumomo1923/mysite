from django.db import models
class Question(models.Model):
    question_text = models.CharField("학습자 번호", max_length=200, null=True, default="")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, default="")
    choice_text = models.CharField("리커트 척도", max_length=200, null=True, default="")
    votes = models.IntegerField(null=True, default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice_text


class Item(models.Model):
    item_type = models.CharField("평가 대상 종류(단어, 문장)", max_length=200, null=True, default="")
    eval_component = models.CharField("평가 요소", max_length=200, null=True, default="")
    item_text = models.CharField("평가 단어/문장", max_length=200, null=True, default="")
    audio_file = models.FileField(upload_to="", null=True, default="")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_text


