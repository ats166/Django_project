from django import forms
from .models import Article

# form class
#    - Model 에 없는 값을 입력받고 싶을 때

# Modelform class
#    - Model에 있는 값만 입력 받고 싶을 때

class ArticleForm(forms.ModelForm):
    # 이 클래스를 설명하는 클래스 - Meta

    class Meta:
        model = Article
        # 사용자의 입력을 원하는 필드 종류
        fields = '__all__'