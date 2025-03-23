# --------------------------------------------
# BlockDevice 생성기 (클라우드용)
#
# 입력:
# - name: 공백 없이 3~30자
# - size: 정수, 최소 1GB 이상
# - type: "ssd", "hdd", "nvme" 중 하나
# - description: 최대 300자 이하
#
# 성공 시 "Created" 리턴,
# 실패 시 상세 오류 메시지 리턴
# --------------------------------------------

class BlkDevCreate:
    VALID_TYPES = {"ssd", "hdd", "nvme"} # class 안에서 선언인지는 잘 모르겠네

    def create(self, device: dict) -> str:
        required_fields = {"name", "size", "type", "description"} #필요한 거 다 넣고 하나하나 ㅋㅋ
        missing = required_fields - device.keys() # 4 - 4 가 되어야 정상임
        if missing: # if(0) 이면 == 4개가 다 입력되었다면 
            return f"missing field: {missing.pop()}"  # 다시 코드 짜라는거

        name = device["name"]
        if not isinstance(name, str) or " " in name or not (3 <= len(name) <= 30):
            return "name invalid"

        try:
            size = int(device["size"])
        except Exception:
            return "size invalid"
        if size < 1:
            return "size invalid"

        if device["type"] not in self.VALID_TYPES:
            return "type invalid"

        description = device["description"]
        if not isinstance(description, str) or len(description) > 300:
            return "description invalid"

        # 생성 로직 생략 (실제 클라우드 SDK 호출이 들어갈 자리)
        # DB Call 같은건 개발팀이 했겠지
        # https://carpe08.tistory.com/374
        return "Created"
