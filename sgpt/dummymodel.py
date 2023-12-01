import viewmodel
from typing import Dict

class Dummymodel:
    def __init__(self):
        self.is_entered = False
    
    def enter_prompt(self, question: str, options: Dict[str, str] = {}):
        return "가나다"
