def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
        return None
    
print(divide(10,0))
print(divide(10,2))