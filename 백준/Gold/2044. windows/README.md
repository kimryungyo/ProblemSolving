# [Gold III] windows - 2044 

[문제 링크](https://www.acmicpc.net/problem/2044) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

구현, 정렬

### 제출 일자

2024년 8월 28일 22:15:31

### 문제 설명

<p>text-mode windows의 개발자인 동혁이는 "cascade mode (계단형 배치)" 부분을 코딩하다가 고심에 빠졌다. text-mode windows에서 하나의 window는 다음과 같이 ‘+’, ‘-’, ‘|’, ‘.’, 그리고 알파벳 소문자로 이루어져 있다.</p>

<pre>+--|abcdef|---+
|.............|
|.............|
|.............|
|.............|
+-------------+
</pre>

<p>모든 window는 위와 같은 형태를 지키고 있으며, title을 기록할 수 있을 정도로 window는 넓다. (즉, title의 길이보다 모든 window는 적어도 6 이상은 가로로 길다. +-|, |-+가 들어가야 하므로) title은 가로로 정확히 가운데에 표시되어 있으며, 만일 위의 경우와 같이 window의 길이가 홀수인 경우 오른쪽이 왼쪽보다 하나 더 길다.</p>

<p>text-mode windows의 screen-shot이 주어졌다. 어떤 두 개의 window도 서로 겹치지 않게 배치되어 있다고 하자. 이때, 동혁이를 도와 다음과 같이 "cascade mode"로 window를 정리해 주는 프로그램을 작성하시오.</p>

<ol>
	<li>모든 window의 가로, 세로 크기는 변하지 않아야 한다.</li>
	<li>모든 window들은 title의 알파벳 순서로 정렬한다.</li>
	<li>모든 window들을 왼쪽 위 꼭짓점이 화면 전체의 왼쪽 위 꼭짓점이 되도록 옮긴다. 그리고 나서, 순서대로 한 칸씩 오른쪽 아래로 내려 배치한다.</li>
</ol>

### 입력 

 <p>첫째 줄에 스크린의 세로 길이 M과 가로 길이 N이 주어진다. (10≤M, N≤100) 이어서 M개의 줄에는 각각 N개의 문자열이 주어지는데, 이는 screen-shot을 나타내 주는 정보이다. 배경 그림 같은 것은 없고 모두 ‘.’으로 표시되며, 모든 window의 title의 길이는 1 이상 10 이하이다. M과 N은 "cascade mode"로 window를 모두 정리할 수 있을 만큼 충분히 크다고 가정해도 좋다.</p>

### 출력 

 <p>M개의 줄에 걸쳐 "cascade mode"로 window를 모두 정리한 화면을 출력한다.</p>

