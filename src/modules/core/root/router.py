from fastapi import APIRouter
from modules.core.root.controller import root_controller

router = APIRouter()


@router.get('/')
def root():
    return root_controller()
