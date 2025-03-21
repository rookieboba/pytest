# src/validate.py

class UserValidator:
    def validate_users(self, users: list[dict]) -> list[str]:
        results = []

        for user in users:
            try:
                username = user["username"]
                age_str = user["age"]
                email = user["email"]
            except KeyError:
                results.append("missing field")
                continue

            try:
                age = int(age_str)
            except ValueError:
                results.append("age invalid")
                continue

            if " " in username:
                results.append("username invalid")
                continue
            if not 3 <= len(username) <= 12:
                results.append("username invalid")
                continue
            if not 0 <= age <= 150:
                results.append("age invalid")
                continue
            if "@" not in email or "." not in email:
                results.append("email invalid")
                continue

            results.append("Valid")

        return results
