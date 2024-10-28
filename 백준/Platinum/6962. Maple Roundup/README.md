# [Platinum V] Maple Roundup - 6962 

[문제 링크](https://www.acmicpc.net/problem/6962) 

### 성능 요약

메모리: 114620 KB, 시간: 152 ms

### 분류

볼록 껍질, 기하학

### 제출 일자

2024년 10월 19일 15:41:32

### 문제 설명

<p style="text-align: center;"><img alt="" src=""></p>

<p>An Elmira area maple syrup producer was selected as the winner of this year's CCC (Canadian Confectionery Competition) and the judge wants to place a blue ribbon around the sugar bush. To do this, she finds the most northerly tree (if there is more than one most northerly tree, any one will do) and stands at the position of that tree, facing due East. She then turns to the right until she is facing another tree, and walks to that tree in a straight line, measuring the distance. Once again she turns right until she faces a tree, and walks to it. At each step she chooses the tree that involves turning the least angle to the right, continuing until the starting tree is reached. The total distance travelled is the length of ribbon required. Your task is to calculate this length.</p>

### 입력 

 <p>The input to the program will consist of a line containing an integer $m$ followed by $m$ data sets. Each data set consists of a line containing an integer $1 < n < 100$, the number of trees in the bush, and this is followed by $n$ lines each with an ordered pair $(x, y)$ of integers which give the location of a tree on the Cartesian grid. You may assume that the $y$-axis points North while the $x$-axis points East.</p>

### 출력 

 <p>For each test case, the output from the program is the length of ribbon, to $2$ decimal places, that can enclose every tree.</p>

