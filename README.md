# our-kitchen

## 공통

- 패키지는 `pip freeze > requirements.txt` 로 저장 및 공유하기. 모든 패키지 한꺼번에 설치 시 `pip install -r requirements.txt`
- 가상환경은 venv 사용하기 
- 각자 맡은 feature 별 브랜치로 작업하고, master 브랜치에서 합치기

## Git 협업 방식

1. 작업 시작할 때 `git pull origin master`로 master 브랜치 소스 동기화
2. 작업 끝날 때도 역시 또 한번 master 브랜치 동기화
3. 동기화가 모두 끝나면 git push origin [각자 브랜치] 로 리모트에 푸시
4. 각자의 브랜치 -> master 브랜치로 PR
5. PR merge(모두 머지할 수 있도록 허용)
