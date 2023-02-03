from fastapi import FastAPI

app = FastAPI(title='The title',
              description='The description',
              version=1)

@app.get('/')
async def index():  # For asynchronous answer
    return 'Hello world'

@app.get('/about')
def about():  # Conventional answer
    return 'The content of about'