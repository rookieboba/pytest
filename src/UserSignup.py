# src/UserSignup.py

class UserSignup:
    REQUIRED_FIELDS = {"username", "password", "email", "gender"}
    VALID_GENDERS = {"M", "W"}

    def signup(self, user: dict) -> str:
        missing = self.REQUIRED_FIELDS - user.keys()
        if missing:
            return f"missing field: {missing.pop()}"

        if not self._is_valid_username(user["username"]):
            return "username invalid"

        if not self._is_valid_password(user["password"]):
            return "password invalid"

        if not self._is_valid_email(user["email"]):
            return "email invalid"

        if not self._is_valid_gender(user["gender"]):
            return "gender invalid"

        # TODO: 실제 회원가입 처리 로직 (DB, 이메일 등)
        return "Signup Successful"

    def _is_valid_username(self, username) -> bool:
        return isinstance(username, str) and 3 <= len(username) <= 20 and " " not in username

    def _is_valid_password(self, password) -> bool:
        return isinstance(password, str) and len(password) >= 6

    def _is_valid_email(self, email) -> bool:
        return isinstance(email, str) and "@" in email and "." in email

    def _is_valid_gender(self, gender) -> bool:
        return gender in self.VALID_GENDERS

# if __name__ == "__main__":
#     user = {
#         "username": "sungbin",
#         "password": "secure123",
#         "email": "sungbin@example.com",
#         "gender": "M"
#     }

#     service = UserSignup()
#     result = service.signup(user)
#     print(result)  # → "Signup Successful"
