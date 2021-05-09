# make_order() 정의 부분

b=list()

def make_order():
    for i in range(4):
        a=int(input('품목을 입력해주세요: '))
        print(b)
        while a<-1 or a>4 or a==0 or a in b:
            print('다시 입력해주세요')
            a=int(input('품목을 입력해주세요: '))
        if a==-1:
            if len(b) == 0:
                print('다시 입력해주세요. 장바구니가 비었습니다')
                continue
            else :
                break
        b.append(a)
    return b

def make_order_new():
    while len(b) < 4:
        품목 = int(input('품목을 입력해주세요: '))
        if 품목 not in range(1, 5) or 품목 in b:
            if 품목 == -1:
                if len(b) == 0:
                    print('다시 입력해주세요. 장바구니가 비었습니다.')
                    continue
                else :
                    break
            continue
        b.append(품목)
    print(b)
    return b
    

# compute_item() 정의 부분

def compute_item(b):
    c=0
    for i in range(len(b)):
        if b[i-1]==1:
            c+=1000
        elif b[i-1]==2:
            c+=1500
        elif b[i-1]==3:
            c+=1200
        elif b[i-1]==4:
            c+=2000
    return c


# main 프로그램 부분
item_list=make_order_new()
print("총합: ",compute_item(item_list))