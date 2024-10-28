import sys
input = sys.stdin.read
data = input().strip().split('\n')

T = int(data[0])
results = []

for i in range(1, T + 1):

    sentence = data[i]
    words = sentence.split()
  
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    results.append(reversed_sentence)

for result in results:
    print(result)