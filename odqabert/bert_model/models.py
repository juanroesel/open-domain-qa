from django.db import models


class QAInput(models.Model):
    question = models.TextField(max_length=512)
    context = models.TextField(max_length=512)

    def __str__(self):
        return self.question + " / " + self.context 

