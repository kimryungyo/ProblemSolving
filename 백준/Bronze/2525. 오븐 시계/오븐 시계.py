A, B = map(int, input().split())
C = int(input())

total_minutes = A * 60 + B

total_minutes += C

end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print(end_hour, end_minute)