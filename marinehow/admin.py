from django.contrib import admin
from .models import Usuario, Question, Answer, Comment
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
