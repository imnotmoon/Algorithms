def checkLen(a):
    if len(a) > 15 :
        return True
    return False

while True:
    if checkLen(input("문자열을 입력하세요 : ")):
        print("통과되었습니다.")
        break
    print("다시 입력해주세요.")
