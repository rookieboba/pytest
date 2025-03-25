# src/VirtualMachineCreate.py

class VirtualMachineCreate:
    # 필수 입력 필드 목록
    REQUIRED_FIELDS = {"name", "image", "cpu", "memory", "network", "disk_size"}

    def create(self, vm: dict) -> str:
        # 필수 필드 누락 체크
        missing = self.REQUIRED_FIELDS - vm.keys()
        if missing:
            return f"missing field: {missing.pop()}"

        # name 유효성 검사
        if not isinstance(vm["name"], str) or len(vm["name"]) < 3 or " " in vm["name"]:
            return "name invalid"

        # image는 반드시 prolinux8.6 이어야 함
        if vm["image"] != "prolinux8.6":
            return "image invalid"

        # cpu는 1 이상 정수
        if not isinstance(vm["cpu"], int) or vm["cpu"] <= 0:
            return "cpu invalid"

        # memory는 1GB 이상 정수
        if not isinstance(vm["memory"], int) or vm["memory"] < 1:
            return "memory invalid"

        # network는 문자열이며 "enp" 또는 "ens"로 시작해야 함
        if not isinstance(vm["network"], str) or not (vm["network"].startswith("enp") or vm["network"].startswith("ens")):
            return "network invalid"

        # disk_size는 10GB 이상 정수
        if not isinstance(vm["disk_size"], int) or vm["disk_size"] < 10:
            return "disk_size invalid"

        # description은 선택이며, 있으면 문자열이고 5000자 이하
        if "description" in vm:
            if not isinstance(vm["description"], str) or len(vm["description"]) > 5000:
                return "description invalid"

        # TODO: 실제 VM 생성 로직 위치
        return "VM Created"

if __name__ == "__main__":
    vm = {
        "name": "vm-sungbin",
        "image": "prolinux8.6",
        "cpu": 4,
        "memory": 8,  # 단위: GB
        "network": "enp0s3",
        "disk_size": 100,
        "description": "성빈의 테스트 가상머신입니다."
    }

    creator = VirtualMachineCreate()
    result = creator.create(vm)
    print(result)  # → "VM Created"
