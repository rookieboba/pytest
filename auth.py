class AuthService:
    """간단한 로그인 검증 시스템"""

    def __init__(self):
        self.users = {"user1": "password123", "admin": "adminpass"}

    def login(self, username, password):
        """사용자가 올바른 계정 정보로 로그인하는지 검증"""
        if username in self.users and self.users[username] == password:
            return "로그인 성공"
        return "로그인 실패"
