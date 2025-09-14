# DP2 알고리즘
DP2 알고리즘은 일반적인 동적 계획법(DP1)보다 복잡한 구조를 가진 문제를 해결할 때 사용하는 기법입니다.

핵심 아이디어: 문제를 두 가지 경우로 나누고, 각각의 경우에 대해 독립적인 DP 테이블을 만든 후, 최종 결과를 두 DP 중 더 좋은 값으로 선택합니다.

주로 원형 구조, 양쪽 끝 조건, 두 가지 선택지가 존재하는 문제에서 사용됩니다.

DP 상태가 2차원 이상이거나, 시작/끝 조건을 달리해야 할 때 효과적입니다.

### 예시 상황:

House Robber II

집들이 원형으로 배치되어 있어 첫 번째 집과 마지막 집은 동시에 털 수 없음

해결법:

첫 집을 포함하지 않는 경우

첫 집을 포함하고 마지막 집은 포함하지 않는 경우
→ 두 가지 경우를 각각 DP로 계산 후, 더 큰 값을 선택

Interleaving String

두 문자열 s1, s2로 s3를 만들 수 있는지 판별

상태를 2차원으로 정의 (dp[i][j] = s1의 i개, s2의 j개로 s3의 i+j 문자 만들 수 있는가)

# 문제
https://leetcode.com/problems/house-robber-ii/description/
https://leetcode.com/problems/interleaving-string/description/
