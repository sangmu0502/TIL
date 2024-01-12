# git
----
### git이란 ?
- 분산 버전 관리 시스템 

### 버전 관리란 ? 
- 변화를 기록하고 추적하는 것

---

#### 중앙 vs 분산
> 중앙 집중식 이란 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드 하는 것이다.

> 분산식은 버전을 여러 개의 복제된 저장소스에 저장 및 관리 하는 것이다.

### 장점
- 중앙 서버에 의존 x

## GIT의 역할
- 코드의 버전을 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교

## GIT의 3가지 영역
- Working Directory
- Staging Area
- Repository

### Working Directory
- 실제 작업 중인 파일들이 위치하는 영역

### Staging area
- Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

### Repository
- 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역 모든 버전과 변경 이력이 기록됨

#### commit
- "버전" 변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 'snapshot'이라고도 함

# git 명령어
---

### git init
- 로컬 저장소 설정(초기화)
- git의 버전 관리를 시작할 디렉토리에서 진행

### git add
- 변경사항이 있는 파일을 staging area에 추가

### git commit
- staging area에 있는 파일들을 저장소에 기록
- 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
- commit 이란 의미있는 변경 작업들을 저장소에 기록하는 동작

### git remote
- git remote add origin remote_repo_url
- 로컬 저장소에 원격 저장소 주소 추가
- origin = 추가하는 원격 저장소의 닉네임
- git remote -v 실행 시 연결 된 저장소가 있으면 보여줌

### fetch

### push
- git push -u origin master
- -u = upstream
- 원격 저장소에 commit 목록을 업로드

### clone
- git clone remote_repo_url
- pull = remote되어있는걸 merge 하는 것
- clone = 세상에 없는 것을 하나 더 만드는 것. clone 해오면 git init을 할 필요 없음.
올려 놓은 사람이 git_practice 폴더를 사용했다면 clone 해오는 사람은 repo 이름의 폴더가 생성된다.
- 차이점 : clone은 local에 없을 때 할 수 있음. git repo가 없는 상태에서.

### gitignore
- git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일
- 프로젝트를 하다보면 프로젝트를 돌아가는데 관련된 파일이 있고 환경과 관련된 파일이 있다. 환경과 관련된 파일은 프로젝트 협업에 방해가 된다.
1. .gitignore 파일 생성 (파일명 앞에 '.' 입력, 확장자 없음)
2. a와 b 이름을 가진 텍스트 파일 생성
3. gitignore에 a.txt 작성
4. gitinit
5. git status

#### 주의사항
- 이미 git의 관리를 받은 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음
- [gitignore 설정 서비스](https://www.toptal.com/developers/gitignore/) 내가 사용하는 언어들을 ctrl + a 해서 gitignore에 복사하자.

# github 활용하기
-  TIL(Today I Learned)을 통해 내가 학습하는 것을 기록
- 개발 면접 지원 시 본인의 github 주소를 공유해 어떤 프로젝트들을 진행했고, 어떤 코드를 작성했는지 공유하고 평가 받기 위해 사용
- 오픈 소스 프로젝트에 기여


# 연습
---

> a.txt, b.txt, a.txt를 수정한 update.txt 만들기

1. mkdir git_commit
2. cd git_commit
3. git init
4. touch a.txt
5. git add a.txt
6. git commit -m 'a.txt'
7. git log 해서 확인
8. touch b.txt
9. git add b.txt
10. git commit -m 'b.txt'
11. git log --oneline 해서 확인
12. a.txt 들어가서 내용 수정.
13. git status  > modified 확인
14. git add .
15. git commit -m 'update.txt'
16. git log --oneline

> 잘못된 파일명 수정하기.

1. git add .
2. git commit -m 'update3.txt'
3. git log --oneline   쳐서 확인 >> update3로 저장돼있음
4. git commit --amend   키보드 i = insert , shift + ; = 명령어 입력 가능 , q = quit
5. git log --oneline 입력해서 수정 됐나 확인.

## remote repository
- 원격 저장소라고도 하며 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간. ex) GitLab, GitHub, Bitbucket
 
 



### 참고 사이트
[git](https://git-scm.com/book/ko/v2)

