def solution(gems):
    answer = []
    gemKind = set(gems)
    start, end = 0, 0
    shortest = len(gems)+1
    
    gemDict = {}
    while(end < len(gems)):
        if gems[end] not in gemDict:
            gemDict[gems[end]] = 1
        else :
            gemDict[gems[end]] += 1
        end += 1

        if len(gemDict) == len(gemKind):
            while(start < end) :
                if gemDict[gems[start]] > 1:
                    gemDict[gems[start]] -= 1
                    start += 1
                elif shortest > end-start:
                        shortest = end-start
                        answer = [start+1, end]
                        break
                else :
                    break

    print(answer)
    return answer


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
