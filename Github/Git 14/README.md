0. github CLI를 가지고 진행해봅시다.
   
    https://cli.github.com/

1. 다음의 깃헙 레포지토리를 fork 한 후 원하는 로컬 경로에 clone 하기
   
    (GitHub 사이트에서 다음의 레포지토리를 fork 합니다. 이 때 "main만 fork 하기" 체크박스 체크하기.)
    
    https://github.com/dla020501/git14-test.git
    
    (로컬에서 경로 이동 후)
    
    `gh repo clone {fork 한 본인의 레포지토리 주소}`

2. test.py를 수정해보기   
   * 처음에는 test 변수를 홀수로 수정하고 commit - push - PR을 해봅시다
        
        `git commit -am "{본인이름}_error"`
        
        `git push`
        
        `gh pr create` <- Title: {본인이름}_error, Body: Skip 해도 됨, What's next?: Submit을 선택
                
    * 이번에는 test 변수를 짝수로 수정하고 commit - push - PR을 해봅시다
        
        `git commit -am "{본인이름}_good"`
        
        `git push`
        
        `gh pr create` <- Title: {본인이름}_good, Body: Skip 해도 됨, What's next?: Submit을 선택        

3. GitHub 사이트에서 본인이 만든 PR 부분을 캡처 후 제출