from fastapi import APIRouter
from stockpredictions.services import DataService

data_router = APIRouter()
data_service = DataService()

@data_router.get('/data/supported-stocks', tags=['Data'])
async def get_supported_stocks():
    return data_service.get_supported_stocks()

@data_router.put('/data/update-last/{ticker}', tags=['Data'])
async def update_last_price(ticker: str):
    return data_service.update_last(ticker)

@data_router.post('/data/save-last/{ticker}', tags=['Data'])
async def update_last_price(ticker: str):
    return data_service.save_last(ticker)

@data_router.post('/data/fill-history/{ticker}', tags=['Data'])
async def fill_history(ticker: str):
    return data_service.fill_history(ticker)