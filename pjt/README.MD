# A. base.html

- 공통 부모 템플릿은 반복적으로 만들어봐서 구현하는데 어려움을 느끼지 못했습니다.

# B. index.html

- index 페이지를 구현하기 위해 new를 통해 Movie의 데이터 베이스에 저장을 하는법이 익숙하지 않아 헷갈렸습니다.

# C. detail.html

- 데이터 베이스의 pk를 이용해 detail페이지에 이미지, 관객수 등 데이터를 출력하는건 어렵지 않았지만, edit, delete를 구현하는데 movie.pk와 views에서 edit, update를 구현하는데 어려움을 겪었습니다.

# D. new.html

- score 타입을 number로 하니 정수형만 입력이 가능한 문제가 발생하여 step=0.1 을 추가하여 0.1씩 조정할 수 있게 했습니다.

# E. edit.html

- Release_date의 초기 value값이 다른것들과 다르게 저장이 되어서 필터를 이용해 값을 넣었습니다.

- genre의 초기값이 디테일의 genre값과 관계없이 comedy로 고정되는 문제가 있어 새로운 옵션을 만들어 genre값을 할당했습니다.