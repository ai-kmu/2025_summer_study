1. 내용 확인하며 hunk별로 스테이징하기
- 아래와 같이 or 아무렇게나 내용 변경

Tigers 변경
* manager: Thanos
* coach: Ronan
* 새 members: Gamora, Nebula
Leopards 변경
* manager: Peter
* coach: Rocket
* 새 members: Drax, Groot

- hunk별로 자유롭게 스테이징 진행 (y/n 하는 부분 캡쳐 1)
- 변경 사항 확인하고 커밋하기 ( `git commit -v` )


2. Stash 써보기
- Leopards의 members에 Stash2 추가
- Jaguars의 members에 Stash3 추가
- `git stash -p`를 사용하여 원하는 것만 stash 하기
- `git stash list`를 사용하여 stash들 확인하기 (캡쳐 2)
- 새로운 new-branch를 만들어서 거기서 `git stash pop` 사용하여 불러와보기

3. Git rebase를 사용하여, 실습처럼 다 바꿔보기
- `git rebase -i` 를 서용해서 여러 커밋을 수정해보기 (아무렇게나) (캡쳐 3)
- 소스트리나 vsc에서 원본 그래프랑 수정 후 그래프 바뀌는거 보기
