from django.contrib import admin
from .models import Question
from .models import Choice
from .models import Eval_item_word
from .models import Eval_item_sentence


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Eval_item_word)
admin.site.register(Eval_item_sentence)