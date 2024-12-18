# vLLM 도커 배포

https://youtu.be/Q99WfdcACyY

지난 시리즈들을 통해 vLLM으로 Llama-3.1-8B를 구동하여 FastAPI를 통해 프롬포트를 받을 수 있는 스크립트를 구성했습니다.

이제는 이 환경을 Docker로 배포하는 방법을 알아보겠습니다. 단, LLM의 경우 모델 내부에 포함시키지 않고 외부에서 마운팅을 통해 언제든지 모델을 변경할 수 있도록 설정하고, 이미지를 생성하는 시간을 최소화 시키겠습니다.

## 디렉토리 구조

- llama : Llama-3.1-8B 모델 다운로드 스크립트
- make_docker : vLLM, FastAPI 기반 vLLM 서빙 환경 도커 이미지 생성
- run_docker : 생성된 도커 이미지 구동 방법

## 이미지 생성 트러블슈팅

- BASE 이미지 문제 :

  python3-slim과 같은 BASE 이미지는 사용이 불가능합니다. 기본적은 ubuntu20.04 환경을 추천드리며 필수적으로 nvidia-cuda가 적용된 이미지를 사용해야 합니다. (디렉토리 내 정의된 Dockerfile을 통해 확인하실 수 있습니다.)

- 도커 실행시 공유 메모리 문제 :

  LLM을 서빙하기 위해선 시스템 공유 메모리에 대한 넉넉한 할당이 요구됩니다. 8G 이상 추천드립니다. (디록토리 내 정의된 run_docker.sh를 통해 확인하실 수 있습니다.)

---
