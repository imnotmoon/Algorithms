def solution(n, lost, reserve):
    answer = 0
    for i in lost :
        if i in reserve: 
            reserve.remove(i)
            lost.remove(i)
    
    for i in range(n):
        student = i+1
        
        # 체육복을 가져온 경우
        if student not in lost : 
            answer += 1
            print(student, " attend to class")
        else :
            # 체육복을 가져오지 않은 경우
            if student-1 in reserve:
                answer += 1
                print(student, " attend to class !!")
                reserve.remove(student-1)
            elif student in reserve :
                answer += 1
                print(student, " attned to class !!!")
                reserve.remove(student)
            elif student+1 in reserve :
                answer += 1
                print(student, " attend to class !!!!")
                reserve.remove(student+1)
            print(reserve)
            
    return answer