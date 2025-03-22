# --------------------------------------------
# 로그인 이력 유효성 검사기 (LoginHistoryValidator)
#
# 사용자 로그인 이력은 다음 조건을 만족해야 함:
# 1. 필드 누락 여부 확인 ("username", "gender", "ip" 필수)
# 2. username: 공백 포함 불가, 길이 3~15자
# 3. gender: "M" 또는 "W"만 허용
# 4. ip: IPv4 형식 유효성 검사 (ipaddress.IPv4Address)
# 검사 실패 시 각 항목에 대해 명시적 메시지 반환
# --------------------------------------------

from typing import List
import ipaddress

class LoginHistoryValidator:
    def validate_logins(self, logs: List[dict]) -> List[str]:
        results = []

        for log in logs:
            # 필드 누락 확인
            for field in ["username", "gender", "ip"]:
                if field not in log:
                    results.append(f"missing field: {field}")
                    break
            else:
                username = log["username"]
                gender = log["gender"]
                ip = log["ip"]

                # username 검사
                if " " in username:
                    results.append("username invalid: contains space")
                    continue
                if len(username) < 3:
                    results.append("username invalid: too short")
                    continue
                if len(username) > 15:
                    results.append("username invalid: too long")
                    continue

                # gender 검사
                if gender not in ("M", "W"):
                    results.append("gender invalid: must be 'M' or 'W'")
                    continue

                # ip 검사
                try:
                    ipaddress.IPv4Address(ip)
                except ValueError:
                    results.append("ip invalid: not a valid IPv4 address")
                    continue

                # 모든 조건 통과
                results.append("Valid")

        return results
