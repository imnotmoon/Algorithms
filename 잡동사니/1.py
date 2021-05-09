def solution(s):
    answer = 0
    answer = s.replace("zero", "0").replace("one", "1").replace("two","2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7")
    answer =answer.replace("eight", "8").replace("nine", "9")
    answer = int(answer)
    print(answer)
    return answer

solution("one4seveneight")
solution("23four5six7")
solution("2three45sixseven")
solution("123")