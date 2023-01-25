from src.utils import PIPELINE

def get_offensive_score(sentence : str) -> dict:

    return PIPELINE(sentence)[0]
    
    


