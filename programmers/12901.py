def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 30, 31]
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = b
    for i in month[:a]:
        day += i
    # print(week[day % 7-1])
    answer = week[day % 7-1]
    return answer


solution(5, 24)
