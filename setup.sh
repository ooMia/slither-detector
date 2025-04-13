#!/bin/bash

# 경로 상수 정의
VENV_SLITHER_PATH=".venv/lib/python3.13/site-packages/slither/detectors"
DETECTORS_DIR="__detectors__"
ALL_DETECTORS_FILE="${DETECTORS_DIR}/all_detectors.py"

# 디렉토리가 없으면 생성
mkdir -p "${DETECTORS_DIR}"

# 1. Slither의 all_detectors.py를 프로젝트 디렉토리로 복사 (없는 경우)
if [ ! -f "${ALL_DETECTORS_FILE}" ]; then
    echo "📥 ${ALL_DETECTORS_FILE} 파일이 없습니다. Slither에서 복사합니다."
    cp "${VENV_SLITHER_PATH}/all_detectors.py" "${ALL_DETECTORS_FILE}"
    
    if [ $? -ne 0 ]; then
        echo "❌ 파일 복사 실패: Slither 설치를 확인해주세요."
        exit 1
    fi
    echo "✅ 복사 완료"
fi

# 2. 커스텀 detector 파일들을 Slither에 적용
echo "🔄 커스텀 detector를 Slither에 적용합니다."
cp "${ALL_DETECTORS_FILE}" "${VENV_SLITHER_PATH}/all_detectors.py"
cp -r "${DETECTORS_DIR}" "${VENV_SLITHER_PATH}/"

if [ $? -ne 0 ]; then
    echo "❌ 적용 실패: 권한 문제가 있는지 확인해주세요."
    exit 1
fi

echo "✅ 설정이 완료되었습니다."