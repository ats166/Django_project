from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# User 재정의 후 장고의 기존 Form 사용 시
# default 로 사용하던 'auth.Form'이 아니므로 에러가 발생함
# 새로 정의한 'accounts.User'를 생성할 수 있도록 Form 재정의
# 아래 코드 : 기존 'auth.forms' 에서 사용하는 UserCreationForm 의 기능을 모두 
# (meta class포함) 가져와서 model만 우리가 정의한 모델로 바꿔줌
# -> 모든 기능을 그대로 사용함
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['email', 'first_name']