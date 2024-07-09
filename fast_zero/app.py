from fastapi import FastAPI

app = FastAPI()


@app.get('/Jesus')
def read_root():
    return {'message': 'EU sou vencedor em Cristo Jesus'}
