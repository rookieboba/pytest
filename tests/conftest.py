import logging
import os
from datetime import datetime

def pytest_configure(config):
    """pytest 실행 시 공통적으로 적용되는 설정"""
    log_dir = "tests/log"
    os.makedirs(log_dir, exist_ok=True)  # log 디렉터리 생성 (없으면 자동 생성)

    log_filename = os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    file_handler = logging.FileHandler(log_filename, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))

    logger = logging.getLogger()
    logger.addHandler(file_handler)
