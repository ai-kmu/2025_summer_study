**깃허브에 올려놓은 실습파일(git-branch)을 이용하여 진행**

## 문제 :
1. main브랜치와 practice브랜치를 fastforward를 이용하지 않고 병합 커밋을 만들어 merge를 진행하세요.
```bash
git merge —no-ff <병합할 브랜치명>
```

2. fruit브랜치 안의 citrus브랜치를 main브랜치로 가져온 후 fastforward병합을 진행하세요.

```bash
git rebase --onto <도착 브랜치> <출발 브랜치> <이동할 브랜치>
```
```bash
git switch main
```
```bash
git merge <병합할 브랜치명>
```
3. Apple커밋의 태그(v0.0.0)을 삭제하세요.
```bash
git tag -d <태그명>
```
4. Lemon커밋에 annotated 태그(v1.0.0)를 생성하고 메세지는 본인의 이름으로 설정하세요.
```bash
git tag <태그명> <Lemon커밋의 해쉬주소> -m <본인이름>
```

## 제출 :
결과물 파일을 `.git` 디렉토리를 포함하여 `이름.zip` 파일로 제출
