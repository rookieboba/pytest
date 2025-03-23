# tests/test_BlkCreate.py

import pytest
from src.BlkDevCreate import BlkDevCreate

creator = BlkDevCreate()

# ---------- 정상 케이스 ----------
def test_block_device_created():
    device = {
        "name": "data-volume-1",
        "size": 100,
        "type": "ssd",
        "description": "성빈 테스트 생성 디스크"
    }
    assert creator.create(device) == "Created"

# ---------- 필드 누락 ----------
@pytest.mark.parametrize("device, expected", [
    ({"size": 100, "type": "ssd", "description": "test"}, "missing field: name"),
    ({"name": "vol01", "type": "ssd", "description": "test"}, "missing field: size"),
    ({"name": "vol01", "size": 100, "description": "test"}, "missing field: type"),
    ({"name": "vol01", "size": 100, "type": "ssd"}, "missing field: description"),
], ids=["missing name", "missing size", "missing type", "missing description"])
def test_missing_fields(device, expected):
    assert creator.create(device) == expected

# ---------- 이름 유효성 ----------
@pytest.mark.parametrize("name, expected", [
    ("a", "name invalid"),
    ("name with space", "name invalid"),
    ("x" * 35, "name invalid"),
], ids=["too short", "contains space", "too long"])
def test_invalid_name(name, expected):
    device = {"name": name, "size": 50, "type": "ssd", "description": "설명"}
    assert creator.create(device) == expected

# ---------- 사이즈 유효성 ----------
@pytest.mark.parametrize("size, expected", [
    (0, "size invalid"),
    (-5, "size invalid"),
    ("fifty", "size invalid"),
], ids=["zero", "negative", "non-integer"])
def test_invalid_size(size, expected):
    device = {"name": "vol-test", "size": size, "type": "ssd", "description": "설명"}
    assert creator.create(device) == expected

# ---------- 타입 유효성 ----------
@pytest.mark.parametrize("dtype, expected", [
    ("tape", "type invalid"),
    ("", "type invalid"),
], ids=["unsupported type", "empty type"])
def test_invalid_type(dtype, expected):
    device = {"name": "vol-test", "size": 50, "type": dtype, "description": "설명"}
    assert creator.create(device) == expected

# ---------- 설명 유효성 ----------
@pytest.mark.parametrize("desc, expected", [
    ("a" * 301, "description invalid"),
    (12345, "description invalid"),
], ids=["too long", "not a string"])
def test_invalid_description(desc, expected):
    device = {"name": "vol-test", "size": 50, "type": "ssd", "description": desc}
    assert creator.create(device) == expected
