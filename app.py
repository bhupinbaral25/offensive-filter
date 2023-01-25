from fastapi import FastAPI

from src.decorator import error_handler
from src.preprocess import clean_sentences
from src.filter_offensive import get_offensive_score
from src.sentence_model import ChatQuery, OutputResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@error_handler
@app.post("/filter/")
async def get_filter(query: ChatQuery):
    """
    API to get filter the querry.
    It takes query as input and returns the respose of that is offensive or not.
    """
 
    filter = get_offensive_score(clean_sentences(query.chat))

    response_body = {
        "offensive": True if filter['label'] == "offensive" else False,
        "confidence_score": filter["score"]
    }

    return OutputResponse(**response_body)