# [Silver IV] 마지막 문제 - 28110 

[문제 링크](https://www.acmicpc.net/problem/28110) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 9월 24일 23:22:11

### 문제 설명

<p>때는 3023년, PPC 출제진들은 심혈을 기울여 PPC에 출제할 $N$개의 문제를 정했다. 각 문제는 $1$ 이상 $10^9$ 이하의 정수로 표현되는 난이도를 가지고 있으며, $N$개의 문제에 대한 난이도는 모두 다르다. 난이도를 나타내는 수가 낮을수록 쉬운 문제임을 의미한다.</p>

<p>하지만 욕심이 가득한 출제진들은 더욱 완벽한 대회를 만들기 위해 마지막 문제를 추가하려 한다. 출제진들은 다음과 같은 조건을 만족하는 난이도의 문제를 추가할 것이다.</p>

<ul>
	<li>기존 $N$개의 문제와 같은 난이도가 아니어야 한다.</li>
	<li>기존 $N$개의 문제 중 가장 쉬운 문제보다 더 쉽거나 가장 어려운 문제보다 더 어려운 난이도가 아니어야 한다.</li>
</ul>

<p>대회의 난이도 분포를 최대한 고르게 하고 싶은 출제진들은, 위와 같은 조건을 만족하는 난이도의 문제 중 기존 문제들과의 난이도 차이의 최솟값이 가장 커지도록 문제를 낼 것이다. 만약 난이도 차이의 최솟값이 가장 커지는 문제가 여러 개 존재한다면 그중 가장 낮은 난이도의 문제를 출제할 것이다. 출제진이 추가할 마지막 문제의 난이도를 구해 보자!</p>

### 입력 

 <p>첫 번째 줄에 준비된 문제의 수 $N$이 주어진다. ($2 \leq N \leq 3\ 000$)</p>

<p>두 번째 줄에 각 문제의 난이도를 나타내는 $N$개의 정수 $A_1, A_2, \ldots, A_N$이 공백으로 구분되어 주어진다. 모든 $A_i$는 서로 다르다. ($1 \leq A_i \leq 10^9$)</p>

### 출력 

 <p>출제진이 추가할 마지막 문제의 난이도를 출력한다. 만약 출제진이 마지막 문제를 추가할 수 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 출력한다.</p>

