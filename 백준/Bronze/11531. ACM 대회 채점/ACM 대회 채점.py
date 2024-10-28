def calculate_score(logs):
    problem_status = {}  # To track the status of each problem
    problem_time = {}    # To track the time each problem was solved
    problem_wrong_attempts = {}  # To track the number of wrong attempts per problem
    
    for log in logs:
        if log == "-1":
            break
        time, problem, result = log.split()
        time = int(time)
        
        if problem not in problem_status:
            problem_status[problem] = False
            problem_wrong_attempts[problem] = 0
        
        if not problem_status[problem]:
            if result == "right":
                problem_status[problem] = True
                problem_time[problem] = time
            else:
                problem_wrong_attempts[problem] += 1

    total_penalty = 0
    solved_problems = 0
    
    for problem in problem_status:
        if problem_status[problem]:
            solved_problems += 1
            total_penalty += problem_time[problem] + (problem_wrong_attempts[problem] * 20)
    
    return solved_problems, total_penalty


logs = []
while True:
    log = input()
    if log == "-1": break
    logs.append(log)

print(*calculate_score(logs))
