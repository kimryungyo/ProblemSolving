MBTI = input()

MATCHS = {
    'ISTJ': 'ENFP', 'ISFJ': 'ENTP', 'INFJ': 'ESTP', 'INTJ': 'ESFP',
    'ISTP': 'ENFJ', 'ISFP': 'ENTJ', 'INFP': 'ESTJ', 'INTP': 'ESFJ',
    'ESTP': 'INFJ', 'ESFP': 'INTJ', 'ENFP': 'ISTJ', 'ENTP': 'ISFJ',
    'ESTJ': 'INFP', 'ESFJ': 'INTP', 'ENFJ': 'ISTP', 'ENTJ': 'ISFP'
}

print(MATCHS[MBTI])