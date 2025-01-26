# [Gold II] Restore Calculation - 10680 

[문제 링크](https://www.acmicpc.net/problem/10680) 

### 성능 요약

메모리: 32412 KB, 시간: 84 ms

### 분류

다이나믹 프로그래밍, 수학

### 제출 일자

2025년 1월 27일 02:35:32

### 문제 설명

<p>The Animal School is a primary school for animal children. You are a fox attending this school.</p>

<p>One day, you are given a problem called "Arithmetical Restorations" from the rabbit teacher, Hanako. Arithmetical Restorations are the problems like the following:</p>

<ul>
	<li>
	<p>You are given three positive integers, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(A\)</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(B\)</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(C\)</span></mjx-container>.</p>
	</li>
	<li>
	<p>Several digits in these numbers have been erased.</p>
	</li>
	<li>
	<p>You should assign a digit in each blank position so that the numbers satisfy the formula <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(A+B=C\)</span></mjx-container>.</p>
	</li>
	<li>
	<p>The first digit of each number must not be zero. It is also the same for single-digit numbers.</p>
	</li>
</ul>

<p>You are clever in mathematics, so you immediately solved this problem. Furthermore, you decided to think of a more difficult problem, to calculate the number of possible assignments to the given Arithmetical Restorations problem. If you can solve this difficult problem, you will get a good grade.</p>

<p>Shortly after beginning the new task, you noticed that there may be too many possible assignments to enumerate by hand. So, being the best programmer in the school as well, you are now trying to write a program to count the number of possible assignments to Arithmetical Restoration problems.</p>

### 입력 

 <p>The input is a sequence of datasets. The number of datasets is less than 100. Each dataset is formatted as follows.</p>

<pre>A
B
C</pre>

<p>Each dataset consists of three strings, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(A\)</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(B\)</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(C\)</span></mjx-container>. They indicate that the sum of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(A\)</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(B\)</span></mjx-container> should be <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(C\)</span></mjx-container>. Each string consists of digits (<code>0</code>-<code>9</code>) and/or question mark (<code>?</code>). A question mark (<code>?</code>) indicates an erased digit. You may assume that the first character of each string is not <code>0</code> and each dataset has at least one <code>?</code>.</p>

<p>It is guaranteed that each string contains between 1 and 50 characters, inclusive. You can also assume that the lengths of three strings are equal.</p>

<p>The end of input is indicated by a line with a single zero.</p>

### 출력 

 <p>For each dataset, output the number of possible assignments to the given problem modulo 1,000,000,007. Note that there may be no way to solve the given problems because Ms. Hanako is a careless rabbit.</p>

