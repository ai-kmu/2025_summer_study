## 아래 파일을 다운받은 뒤 vscode에 연동해 과제를 수행하세요.
[git-bisect.zip](https://github.com/user-attachments/files/21895572/git-bisect.zip)

### 이진탐색으로 오류 발생 지점 찾기

1. 이진탐색 시작

      ````git bisect start````

2. 현재 오류가 발생했음(error: true)을 표시

      ````git bisect bad````

3. 의심 지점으로 이동 (소스트리 활용)

      ````git checkout (해당 커밋 해시)````

4. 오류 없으면(error: false) 양호함 표시

      ````git bisect good````

5. 오류 발생 지점 발견할 때까지 반복

6. 오류 발생 지점 발견하면 이진탐색 종료

      ````git bisect reset````

### 오류 발생 지점을 찾은 캡쳐 화면을 github에 올리세요.
