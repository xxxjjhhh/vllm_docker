# docker run -d --gpus all --shm-size=용량 -v 외부경로:컨테이너경로 -e MODEL_PATH="컨테이너경로" -p 외부포트:내부포트 도커이미지명
# -d : 백그라운드 실행
# --gpus all : 모든 GPU 사용
# --shm-size=16G : 공유 메모리 설정 (설정 안 할 경우 LLM 구동 불가) free -h로 시스템 메모리 확인 후 적절히 배치
# -v 외부경로:컨테이너경로 : 볼륨 마운트 (여기서 우리 외부의 LLM을 마운팅 하여 컨테이너에서 모델 파일을 사용할 수 있도록 설정)
# -e MODEL_PATH="컨테이너경로" : 위에서 볼륨 마운트를 통해 컨테이너에 마운팅 시킨 모델을 async_server.py 파이썬 스크립트에서 위치를 찾을 수 있도록 환경 변수 설정
# -p 외부포트:내부포트 : 포트포워딩 (FastAPI에서 요청을 받기 위한 포트 포워딩)

docker run -d --gpus all --shm-size=16G -v /home/xxxjjhhh/my_model:/app/models -e MODEL_PATH="/app/models/Meta-Llama-3.1-8B-Instruct/" -p 8080:8080 test_vllm_1