# [Gold II] 조각 체스판 - 22983 

[문제 링크](https://www.acmicpc.net/problem/22983) 

### 성능 요약

메모리: 539496 KB, 시간: 1104 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 7월 22일 01:17:50

### 문제 설명

<p>높이 $N$, 너비 $M$의 정사각형 격자에 검은색과 흰색 중 한 가지 색이 칠해져 있다. 머릿속이 체스로 가득찬 현채는 문득 이 격자를 잘랐을 때 체스판이 되는 경우가 몇 가지인지 궁금해졌다.</p>

<p>체스판은 검은색과 흰색이 번갈아 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 체스판의 모양은 정사각형이어야 하며, 꼭 $8 \times 8$일 필요는 없다.</p>

<p>현채의 궁금증을 해결해 주자.</p>

### 입력 

 <p>다음과 같이 입력이 주어진다.</p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">
<p>$N\ M$<br>
$C_{1,1} C_{1,2} \cdots C_{1,M}$<br>
$C_{2,1} C_{2,2} \cdots C_{2,M}$<br>
$\vdots$<br>
$C_{N,1} C_{N,2} \cdots C_{N,M}$</p>
</div>

<ul>
	<li>$1 \leq N,M \leq 3\,000$</li>
	<li>$C_{i,j}$는 $\left(i,j\right)$에 칠해진 색상을 의미하는 문자이며 <span style="color:#e74c3c;"><code>B</code></span>와 <span style="color:#e74c3c;"><code>W</code></span> 중 하나이다. $C_{i,j}$가 <span style="color:#e74c3c;"><code>B</code></span>라면 $\left(i,j\right)$에 검은색이, <span style="color:#e74c3c;"><code>W</code></span>라면 $\left(i,j\right)$에 흰색이 칠해져 있다.</li>
</ul>

### 출력 

 <p>주어진 격자를 잘랐을 때 체스판이 되는 경우가 몇 가지인지 출력한다.</p>

