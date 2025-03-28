# [Gold IV] 등차수열 - 1345 

[문제 링크](https://www.acmicpc.net/problem/1345) 

### 성능 요약

메모리: 31120 KB, 시간: 36 ms

### 분류

수학

### 제출 일자

2024년 9월 28일 23:19:34

### 문제 설명

<p>수학에서 등차수열은 두 개의 연속된 숫자의 차이가 항상 일정한 수열이다. 예를 들어, 3 5 7 9 11 13은 차이가 2인 등차수열이다. 등차수열은 A<sub>n</sub> = A<sub>0</sub>+n*d와 같이 표현할 수 있다.</p>

<p>수열 S가 주어진다. 수열 S<sub>i</sub> = ⌊A<sub>i+1</sub>⌋이다. 그리고, 감소하지 않는 수열이다. ⌊x⌋는 x보다 작거나 같은 정수 중 가장 큰 값이다. 예를 들어 ⌊3.4⌋ = 3, ⌊0.6⌋ = 0, ⌊-1.2⌋ = -2, ⌊-0.6⌋ = 1이다.</p>

<p>수열 A는 A<sub>0</sub>+i*d와 같이 정의할 수 있다. 가능한 d의 값 중 가장 작은 값을 구하는 프로그램을 작성하시오. d는 0 이상이다.</p>

### 입력 

 <p>첫째 줄에 주어지는 수열 S의 개수 N과 A<sub>0</sub>이 주어진다. 둘째 줄에 S<sub>0</sub>부터 S<sub>N-1</sub>까지 주어진다. N은 0보다 크거나 같고, 50보다 작거나 같은 정수이고, 나머지 수는 모두 절댓값이 10<sup>6</sup>보다 작거나 같은 정수이다. N이 0인 경우 둘째 줄은 주어지지 않는다.</p>

### 출력 

 <p>첫째 줄에 가능한 d중 최솟값을 출력한다. 절대/상대 오차는 10<sup>-9</sup>까지 허용한다. 만약, 그러한 것이 없을 때는 -1을 출력한다.</p>

