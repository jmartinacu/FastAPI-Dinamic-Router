from fastapi import APIRouter

router = APIRouter(
    tags=['auth'],
)


@router.get('/')
def root():
    return 'Hello core auth router!'


@router.get('/hello')
def hello():
    return 'Hello from auth !!'
