# vLLM 도커 배포

https://youtu.be/Q99WfdcACyY

지난 시리즈들을 통해 vLLM으로 Llama-3.1-8B를 구동하여 FastAPI를 통해 프롬포트를 받을 수 있는 스크립트를 구성했습니다.

이제는 이 환경을 Docker로 배포하는 방법을 알아보겠습니다. 단, LLM의 경우 모델 내부에 포함시키지 않고 외부에서 마운팅을 통해 언제든지 모델을 변경할 수 있도록 설정하고, 이미지를 생성하는 시간을 최소화 시키겠습니다.

## 디렉토리 구조

- llama : Llama-3.1-8B 모델 다운로드 스크립트
- make_docker : vLLM, FastAPI 기반 vLLM 서빙 환경 도커 이미지 생성
- run_docker : 생성된 도커 이미지 구동 방법

---
