# tests/test_VirtualMachineCreate.py

import pytest
from src.VirtualMachineCreate import VirtualMachineCreate

vm_creator = VirtualMachineCreate()

# ---------- 정상 케이스 ----------
def test_vm_create_success():
    vm = {
        "name": "vm-test",
        "image": "prolinux8.6",
        "cpu": 2,
        "memory": 4,  # 단위: GB
        "network": "enp0s3",
        "disk_size": 50,
        "description": "테스트용 가상머신입니다."
    }
    assert vm_creator.create(vm) == "VM Created"

# ---------- 필수 항목 누락 ----------
@pytest.mark.parametrize("vm, expected", [
    ({"image": "prolinux8.6", "cpu": 2, "memory": 4, "network": "enp0s3", "disk_size": 50}, "missing field: name"),
    ({"name": "vm01", "cpu": 2, "memory": 4, "network": "enp0s3", "disk_size": 50}, "missing field: image"),
    ({"name": "vm01", "image": "prolinux8.6", "memory": 4, "network": "enp0s3", "disk_size": 50}, "missing field: cpu"),
    ({"name": "vm01", "image": "prolinux8.6", "cpu": 2, "network": "enp0s3", "disk_size": 50}, "missing field: memory"),
    ({"name": "vm01", "image": "prolinux8.6", "cpu": 2, "memory": 4, "disk_size": 50}, "missing field: network"),
    ({"name": "vm01", "image": "prolinux8.6", "cpu": 2, "memory": 4, "network": "enp0s3"}, "missing field: disk_size"),
], ids=["no name", "no image", "no cpu", "no memory", "no network", "no disk_size"])
def test_missing_fields(vm, expected):
    assert vm_creator.create(vm) == expected

# ---------- name 유효성 ----------
@pytest.mark.parametrize("name, expected", [
    ("", "name invalid"),
    ("a b", "name invalid"),
    ("ab", "name invalid"),
], ids=["empty", "contains space", "too short"])
def test_invalid_name(name, expected):
    vm = {
        "name": name,
        "image": "prolinux8.6",
        "cpu": 2,
        "memory": 4,
        "network": "ens33",
        "disk_size": 20
    }
    assert vm_creator.create(vm) == expected

# ---------- image 유효성 ----------
@pytest.mark.parametrize("image, expected", [
    ("", "image invalid"),
    ("ubuntu", "image invalid"),
    ("prolinux9", "image invalid"),
], ids=["empty", "ubuntu", "wrong version"])
def test_invalid_image(image, expected):
    vm = {
        "name": "vm01",
        "image": image,
        "cpu": 2,
        "memory": 4,
        "network": "enp0s3",
        "disk_size": 20
    }
    assert vm_creator.create(vm) == expected

# ---------- cpu 유효성 ----------
@pytest.mark.parametrize("cpu, expected", [
    (0, "cpu invalid"),
    (-1, "cpu invalid"),
    ("two", "cpu invalid"),
], ids=["zero", "negative", "not int"])
def test_invalid_cpu(cpu, expected):
    vm = {
        "name": "vm01",
        "image": "prolinux8.6",
        "cpu": cpu,
        "memory": 4,
        "network": "enp0s3",
        "disk_size": 20
    }
    assert vm_creator.create(vm) == expected

# ---------- memory 유효성 ----------
@pytest.mark.parametrize("memory, expected", [
    (0, "memory invalid"),
    (-1, "memory invalid"),
    ("4096", "memory invalid"),
], ids=["zero", "negative", "not int"])
def test_invalid_memory(memory, expected):
    vm = {
        "name": "vm01",
        "image": "prolinux8.6",
        "cpu": 2,
        "memory": memory,
        "network": "enp0s3",
        "disk_size": 20
    }
    assert vm_creator.create(vm) == expected

# ---------- network 유효성 ----------
@pytest.mark.parametrize("network, expected", [
    ("", "network invalid"),
    ("eth0", "network invalid"),
    ("abc123", "network invalid"),
    (1234, "network invalid"),
], ids=["empty", "not enp/ens", "wrong prefix", "not string"])
def test_invalid_network(network, expected):
    vm = {
        "name": "vm01",
        "image": "prolinux8.6",
        "cpu": 2,
        "memory": 4,
        "network": network,
        "disk_size": 20
    }
    assert vm_creator.create(vm) == expected

# ---------- disk_size 유효성 ----------
@pytest.mark.parametrize("disk_size, expected", [
    (0, "disk_size invalid"),
    (5, "disk_size invalid"),
    ("fifty", "disk_size invalid"),
], ids=["zero", "too small", "not int"])
def test_invalid_disk_size(disk_size, expected):
    vm = {
        "name": "vm01",
        "image": "prolinux8.6",
        "cpu": 2,
        "memory": 4,
        "network": "ens33",
        "disk_size": disk_size
    }
    assert vm_creator.create(vm) == expected

# ---------- description 유효성 ----------
@pytest.mark.parametrize("desc, expected", [
    ("a" * 5001, "description invalid"),
    (12345, "description invalid"),
], ids=["too long", "not a string"])
def test_invalid_description(desc, expected):
    vm = {
        "name": "vm01",
        "image": "prolinux8.6",
        "cpu": 2,
        "memory": 4,
        "network": "ens33",
        "disk_size": 50,
        "description": desc
    }
    assert vm_creator.create(vm) == expected
