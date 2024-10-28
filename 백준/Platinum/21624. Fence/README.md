# [Platinum IV] Fence - 21624 

[문제 링크](https://www.acmicpc.net/problem/21624) 

### 성능 요약

메모리: 147180 KB, 시간: 296 ms

### 분류

볼록 껍질, 기하학

### 제출 일자

2024년 10월 18일 13:59:34

### 문제 설명

<p>Donald owns a nice small house in Manhattan. Due to recent elections it is important to protect yourself from the potential public unrest, so Donald has decided to build a fence around his house.</p>

<p>Donald's house can be represented as a polygon on the plane, with all the coordinates being integers. Moreover, all of his house corners are exactly $90\deg$, and each wall is parallel to either east-west or north-south axis. Donald wants to build a fence so that the house is completely inside of it and that the fence is not too close to the house. More precisely, Donald wants to build a fence in such way that Manhattan distance between any point of the fence and any point of the house is at least $l$.</p>

<p>Recall that Manhattan distance between points $(x_1, y_1)$ and $(x_2, y_2)$ is $|x_1 - x_2| + |y_1 - y_2|$.</p>

<p>Donald wants to minimize building costs, so he asks you to find the smallest possible length of the fence.</p>

### 입력 

 <p>The first line contains integers $n$ and $l$ ($4 \le n \le 100\,000$, $0 \le l \le 10^8$).</p>

<p>Each of the next $n$ lines contains integers $x_i$, $y_i$ ($|x_i|, |y_i| \le 10^8$), describing the border of the house in clockwise or counterclockwise order.</p>

<p>It's guaranteed that the house is non-degenerate, doesn't contain any self-intersections (no two segments intersect except the neighboring segments having a common end), no two points coincide, all the house walls are either vertical or horizontal.</p>

### 출력 

 <p>Print a single real value, the smallest possible length of the fence. Your answer will be considered correct if it's absolute or relative error will be at most $10^{-6}$.</p>

