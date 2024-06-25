from fastapi import APIRouter
from model import AdditionRequest, AdditionResponse
from util import perform_addition
import logging
from datetime import datetime

router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.post("/add", response_model=AdditionResponse)
def add_lists(request: AdditionRequest):
    try:
        started = datetime.now()
        print(request)
        results = perform_addition(request.lists)
        print(results)
        completed = datetime.now()
        return AdditionResponse(batchid=request.batchid, results=results, status="complete",started_at=started,completed_at=completed)
    except Exception as e:
        logging.error(e,exc_info=True)
        return AdditionResponse(batchid=request.batchid,results=[], status=f"error: {str(e)}",started_at=started,completed_at=datetime.now())
