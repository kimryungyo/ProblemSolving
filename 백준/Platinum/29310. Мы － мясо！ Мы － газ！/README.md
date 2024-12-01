# [Platinum IV] Мы - мясо! Мы - газ! - 29310 

[문제 링크](https://www.acmicpc.net/problem/29310) 

### 성능 요약

메모리: 130900 KB, 시간: 376 ms

### 분류

분류 없음

### 제출 일자

2024년 9월 15일 17:30:01

### 문제 설명

<p>Футбольный клуб <<Газмяс>> в этом сезоне тренирует новый тренер, поскольку методами предыдущего тренера руководство и игроки были слегка не довольны. Новый тренер подходит ко всем вопросам с математической точки зрения. Если раньше перед тренировкой игроки собирались в кружок и слушали тренера, то у нового тренера другой подход. Он строит игроков в линию в алфавитном порядке. А так как тренер окончил Институт Точного Математического Образования, он легко может с точностью до сантиметра определить рост каждого игрока.</p>

<p>Далее задача тренера состоит в том, чтобы определить состав на следующую игру. Для этого он хочет определить сколько у него есть пар сыгранных футболистов. Но у нового тренера понятие <<Пара сыгранных футболистов>> очень странно. Два футболиста считаются сыгранными, если при построении в алфавитном порядке игрок с большим ростом стоит левее, чем второй футболист, рост обоих футболистов четен, и между ними стоит хотя бы один футболист с нечетным ростом.</p>

<p>Хотя новый тренер и очень умен, но в этом сезоне состав <<Газмяса>> очень большой (оно и понятно, <<Газмяс>> собирается выйти в Премьер-лигу). Поэтому он не может сам посчитать количество пар и просит Вас помочь ему. Перед тем, как вы приступили к выполению этого ответственного задания, тренер сообщил Ввм, что рост всех игроков различен.</p>

### 입력 

 <p>Первая строка содержит одно число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 10^5$</span></mjx-container>)  --- количество футболистов. Вторая строка содержит <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> чисел, идущих через пробел  --- рост футболистов. Рост каждого футболиста положителен и не превышает <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>. Рост всех футболистов различен. Футболисты уже упорядочены по алфавиту.  </p>

### 출력 

 <p>Выведите одно число  --- количество пар сыгранных футболистов.</p>

