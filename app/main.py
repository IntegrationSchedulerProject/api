from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'FastAPI 설치가 완료되었습니다!'}
