# 시스템에 가입할 때 비밀번호는 다음의 모든 조건을 만족해야 유효합니다:

# 8자 이상, 20자 이하
# 영문 대문자, 소문자, 숫자, 특수문자 중 3종류 이상 포함
# 특수문자는 다음 중 하나여야 함: !@#$%^&*()
# 공백이 포함되면 안 됨
# is_valid_password(password: str) -> bool 함수를 구현하고,
# 적절한 테스트 케이스를 6개 이상 작성하여 검증하세요.

def is_valid_password(password: str) -> bool:
    if not 8 <= len(password) <= 20: # 8자 이상, 20자 이하
        return False
    if " " in password: # 공백이 포함되면 안됨
        return False
    
    has_upper = any(c.isupper() for c in password) #대문자 존재여부. 존재 시 1
    has_lower = any(c.islower() for c in password) #소문자 존재 여부
    has_digit = any(c.isdigit() for c in password) #숫자 존재 여부
    has_special = any(c in "!@#$%^&*()" for c in password) #특수문자 존재 여부

    count = sum([has_upper, has_lower, has_digit, has_special]) #3종류 이상 포함
    if count < 3:
        return False
    
    return True