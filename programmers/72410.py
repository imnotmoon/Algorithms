def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    allow = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_', '.']
    for char in new_id:
        if char not in allow:
            new_id = new_id.replace(char, '')
    # 3
    while('..' in new_id):
        new_id = new_id.replace("..", '.')
    # 4
    if(len(new_id) > 0):
        if new_id[0] == '.':
            new_id = new_id[1:]
    if(len(new_id) > 0):
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 5
    if new_id == "":
        new_id = "a"
    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7
    if len(new_id) < 3:
        new_id = new_id + (new_id[-1]*(3-len(new_id)))

    answer = new_id
    print(answer)
    return answer


solution("abcdefghijklmn.p")
