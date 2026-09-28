from fastapi import APIRouter
router = APIRouter()

@router.get("/health")
def check_health():
    return {"status":"dhere dhere ho jayega"}

@router.get("/health/{server_id}")
def check_server_health(server_id: int):
    return {"status": "dhere dhere ho jayega", "server_id": server_id}
