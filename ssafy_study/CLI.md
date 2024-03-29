# CLI
---
> CLI 란 Command Line Interface 의 약자 이며, **명령어**를 통해 사용자와 컴퓨터가 상호 작용하는 방식이다.

- 요즘은 GUI 시대로 바뀌었다.

## CLI 사용하는 이유
- GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 성능을 상대적으로 더 많이 소모
- 수 많은 서버 / 개발 시스템이 CLI를 통한 조작이 가능

## CLI에서 .(점)의 역할

현재 디렉토리 : .

현재의 상위 디렉토리(부모 폴더) : ..

|명령어|기능|
|:---:|:---:|
|.|현재 작업 중인 디렉토리|
|..|현재 작업 중인 디렉토리의 상위 디렉토리|
|pwd|현재 작업중인 디렉토리 확인|
|cd|change directory|
|touch|파일 생성|
|mkdir|새 디렉토리 생성|
|ls(list)|현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력(-a 옵션을 이용해 숨겨진 파일까지 다 보여줌)|
|start|폴더/파일을 열기 (mac에서는 open)|
|rm|파일 삭제(-r 옵션을 사용해 디렉토리 삭제)|
|mv|파일을 다른 디렉토리로 옮기기|

## 유의점
- 내가 어디 있는지(경로) 알아야 한다.

### 절대 경로
- Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
- 윈도우 바탕화면의 절대 경로 예시 `C:/Users/ssafy/Desktop`
- 다른 서버에 절대 경로를 전달 해주면 작동하지 않는다.

### 상대 경로
- 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
- 만약 현재 작업하고 있는 디렉토리가 `C:/Users`일 때 윈도우 바탕화면으로의 상대 경로는 `ssafy/Desktop`



