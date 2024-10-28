# [Silver IV] 박스 그림 문자 - 23038 

[문제 링크](https://www.acmicpc.net/problem/23038) 

### 성능 요약

메모리: 1908 KB, 시간: 12 ms

### 분류

구현

### 제출 일자

2024년 10월 1일 02:12:01

### 문제 설명

<p>유니코드 문자 중에는 box-drawing character(박스 그림 문자)라는 종류의 문자들이 있다. 이 문자들은 텍스트 UI에서 구역을 나누는 테두리를 그리기 위해 만들어진 것으로, 상하좌우 방향의 선들로 이루어져 있다. 박스 그림 문자의 종류는 다음과 같이 총 $11$가지이다.</p>

<p style="text-align: center;"><strong>┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘ ─ │</strong></p>

<p>이 문자들을 이용하면 다음과 같이 재밌는 모양들을 만들 수 있다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 519px; height: 269px;"></p>

<p>위 모양들은 모두 선이 끊어지는 곳이 없다는 특징이 있다. 예를 들어 어떤 문자가 오른쪽 방향의 선을 갖고 있다면, 그 오른쪽에는 반드시 왼쪽 방향의 선을 갖고 있는 문자가 있다. 이러한 특징을 갖는 모양들을 <strong>아름다운 모양</strong>이라고 하자. 다음은 아름다운 모양이 아닌 모양의 예시이다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 266px; height: 264px;"></p>

<p>실버는 아름다운 모양 하나를 만들어 파일로 저장해 두었다. 하지만 컴퓨터가 바이러스에 감염되어 파일의 일부분이 <code>.</code>으로 날아가버렸다!</p>

<p style="text-align: center;"><img alt="" src="" style="width: 263px; height: 259px;"></p>

<p>다행히도 <code>.</code>으로 대체된 부분들은 체스판처럼 배열되어 있다. 다시 말하면, $i+j$가 홀수일 때 $i$행 $j$열의 문자가 <code>.</code>으로 대체되어 있다. 자신의 작품이 망가져 좌절한 실버를 도와 모양을 복원해 보자. 단, 당신은 박스 그림 문자를 제대로 출력할 줄 모르기 때문에 각 문자들을 다음의 $3 \times 3$ 블록으로 치환하여 입출력할 것이다.</p>

<table align="center" class="table-23038 table table-bordered text-center">
	<tbody>
		<tr>
			<td style="border-top: 1px solid #333;">
			<pre>...
.##
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>...
###
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>...
##.
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>.#.
.## 
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>.#.
###
.#.</pre>
			</td>
			<td style="border-top: 1px solid #333;">
			<pre>.#.
##.
.#.</pre>
			</td>
		</tr>
		<tr>
			<td style="background-color: #eee;">┌</td>
			<td style="background-color: #eee;">┬</td>
			<td style="background-color: #eee;">┐</td>
			<td style="background-color: #eee;">├</td>
			<td style="background-color: #eee;">┼</td>
			<td style="background-color: #eee;">┤</td>
		</tr>
		<tr>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
			<td style="height: 8px; padding: 0; border-top: 1px solid #333; border-bottom: 1px solid #333;"> </td>
		</tr>
		<tr>
			<td>
			<pre>.#.
.##
...</pre>
			</td>
			<td>
			<pre>.#.
###
...</pre>
			</td>
			<td>
			<pre>.#.
##.
...</pre>
			</td>
			<td>
			<pre>...
###
...</pre>
			</td>
			<td>
			<pre>.#.
.#.
.#.</pre>
			</td>
			<td>
			<pre>...
...
...</pre>
			</td>
		</tr>
		<tr>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">└</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">┴</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">┘</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">─</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">│</td>
			<td style="border-bottom: 1px solid #333; background-color: #eee;">.</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄에 실버가 만든 모양의 행 수 $N$과 열 수 $M$이 공백을 사이에 두고 주어진다. ($2 \le N \le 300$, $2 \le M \le 300$)</p>

<p>이후 $3N$개의 줄에 걸쳐 실버가 만든 모양이 주어진다. 각 줄은 $3M$개의 문자로 이루어져 있으며, 각 문자는 <code>.</code> 또는 <code>#</code>이다.</p>

### 출력 

 <p>$3N$개의 줄에 걸쳐 복원된 실버의 작품을 출력한다.</p>

