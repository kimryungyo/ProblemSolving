# [Gold III] 일이 너무 많아... - 24551 

[문제 링크](https://www.acmicpc.net/problem/24551) 

### 성능 요약

메모리: 111420 KB, 시간: 632 ms

### 분류

임의 정밀도 / 큰 수 연산, 포함 배제의 원리, 수학

### 제출 일자

2024년 7월 12일 01:25:37

### 문제 설명

<p style="text-align: center;"><img alt="카카오_지갑_로고" src="" style="max-height:270px; object-fit:contain; display:inline-block;"></p>

<p>카카오에 7년 경력을 가진 신입 개발자로 입사한 pichulia. pichulia 는 카카오 서비스 중 카카오 지갑 서비스 개발 담당자가 되었다.</p>

<p>카카오 지갑은 사용자가 소유한 디지털 자산과 아이템이 담기는 곳으로써 본인 확인을 거쳐 이용할 수 있는 카카오의 다양한 서비스를 모아볼 수 있는 공간이다.</p>

<p>카카오 지갑에서 제공하는 서비스는 매우 다양하다. 우선 '카카오 인증서'를 통해 각종 금융기관과의 연동 서비스를 지원한다. 그리고 '톡명함'을 통해 나를 돋보이게 만드는 명함을 만들 수 있고, 이 명함을 이용해 개발자 커뮤니티 등, 나를 필요로 하는 사람들과 소통할 수 있다. 게다가 '지갑 QR' 을 이용한 무인 매장 이용 서비스도 지원한다. 이 외에도 많은 서비스를 제공하고 있다.</p>

<p>사용자 입장에서는 진짜 지갑처럼 매우 유용하게 사용할 수 있을 것이다. 하지만 개발자 입장에서는 이 모든 것이 정상적으로 돌아가도록 관리를 해야만 하기 때문에 pichulia 는 언제나 일이 많다.</p>

<p>일이 하나만 있는 것도 힘든데, 이렇게 일이 여러 개가 있다... ㅠㅜ</p>

<p>그래서 pichulia 는 $11$, $111$, $1111$, $\cdots$ 와 같이 2개 이상의 숫자 $1$로만 이루어진 수를 싫어한다. 게다가 이러한 수를 약수로 가진 수도 싫어한다.</p>

<p>양의 정수 $N$이 주어졌을 때, $1$ 이상 $N$ 이하의 정수 중 pichulia 가 싫어하는 수의 개수를 구해보자. pichulia 는 위에 서술된 특징을 가진 정수를 제외한 모든 수를 싫어하지 않는다고 가정한다.</p>

### 입력 

 <p>첫 번째 줄에 문제에서 정의된 정수 $N$이 주어진다. ($1 \le N \le 10^{18}$)</p>

### 출력 

 <p>$1$ 이상 $N$ 이하의 정수 중 2개 이상의 숫자 $1$로만 이루어진 수를 약수로 가지는 수의 개수를 출력한다.</p>

