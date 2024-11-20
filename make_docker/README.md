# Dockerfile

## 도커 이미지 생성

<pre><code>
sudo sh make.sh
</code></pre>

## 디렉토리 구조

- async_server.py : FastAPI 및 vLLM 구동 스크립트
- Dockerfile : 도커 이미지 생성용 도커파일
- make.sh : 도커 이미지 생성을 위해 도커 파일 실행용 스크립트 sudo sh make.sh
- README.md : README
- requirements.txt : 도커 이미지 생성시 필요한 파이썬 패키지 목록

---