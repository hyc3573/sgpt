import viewmodel
from typing import Dict
from uuid import uuid4

class Dummymodel:
    def __init__(self):
        self.is_entered = False
    
    def enter_prompt(self, question: str, options: Dict[str, str] = {}):
        return str(uuid4())
