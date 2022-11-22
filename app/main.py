from fastapi import FastAPI

app = FastAPI(
    title='FastAPI-server'
)


@app.get('/')
def index():
    return {'hello': 'world'}