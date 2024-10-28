# [Platinum IV] Art Exhibition - 29944 

[문제 링크](https://www.acmicpc.net/problem/29944) 

### 성능 요약

메모리: 175264 KB, 시간: 892 ms

### 분류

볼록 껍질, 기하학, 다각형의 넓이

### 제출 일자

2024년 10월 19일 02:15:32

### 문제 설명

<p>Once a year contestants from multiple countries gather to compete in the Best Olympiad in Informatics. Besides the competition, guests have an opportunity to visit local museums and landmarks. This year there will be an art exhibition specially made for the contestants and to appeal to such an audience every picture will be a collection of points with integer coordinates.</p>

<p>The coordinates of the points in every picture are already decided on and what's left is to print the pictures out. However, printing them on normal rectangular canvas is wasteful as a large part of the paper might not containt any points at all. To make the exhibition more eco-friendly, every canvas shall be a four-sided polygon with the top and bottom sides completely horizontal. The canvas must contain all points, but at the same time it must be as small as possible.</p>

<p>Your job is to write a program that outputs the minimum possible area of the canvas. Note that any side of the canvas can be infinitely small, making the canvas look like a triangle, line or even a point (in the last two cases the area is zero).</p>

### 입력 

 <p>The first line of input contains the number of points $N$ ($1 \le N \le 10^5$). The next $N$ lines contain two numbers each: the coordinates $x_i$ and $y_i$ of point $i$, in picometers ($-10^8 \le x_i, y_i \le 10^8$).</p>

### 출력 

 <p>On the only line of ouput, output the minimum possible area of the canvas. Your answer will be considered correct if it doesn't differ from the true answer by more than $0.0001\%$.</p>

