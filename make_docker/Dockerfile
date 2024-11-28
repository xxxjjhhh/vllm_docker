# 기본 이미지 : 우분투 환경에서 서빙을 해야하고 NVIDIA CUDA를 지원해야 함, 따라서 아래 주소에서 tag 선택 (python과 같은 기본 이미지 환경 선택시 이미지 구동 오류 발생)
# https://hub.docker.com/r/nvidia/cuda/tags
FROM nvidia/cuda:12.6.2-cudnn-devel-ubuntu22.04

# 도커 컨테이너 기본 루트 디렉토리
WORKDIR /app

# apt 설치 (apt 설치시 콘솔 입력 무시) : 파이썬, pip, ray 설치 (ray는 멀티 GPU 환경을 위해 요구 됨)
RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y python3 python3-pip ray

# 파이썬 패키지 설치 (패키지 목록은 requirements.txt 내부에 명시)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 볼륨 마운트 (실제 Llama3.1 모델의 경우 이미지에 포함을 시키는 것이 아닌 마운트롤 통해 사용할 예정이고, 마운트 경로에 대한 영구적인 VOLUME 설정)
VOLUME ["/app/models"]

# 현재 Dockerfile 디렉토리에 있는 async_server.py와 같은 기본적인 도커 파일을 만들기 위해 필요한 스크립트 도커로 복사
COPY . .

# 도커 컨테이너 실행시 실행할 명령어 (uvicorn 으로 서빙)
CMD ["python3", "-m", "uvicorn", "async_server:app", "--host", "0.0.0.0", "--port", "8080"]
