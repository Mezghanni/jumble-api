import random

from pydantic import validator
from pydantic.main import BaseModel


class Word(BaseModel):
    word: str

    @validator("word")
    def sanitize_word(cls, word):
        if not all(c.isalpha() for c in word):
            raise ValueError("Word must only contain alphabetic characters")
        return word

    def jumble(self):
        chars = list(self.word)
        random.shuffle(chars)
        return "".join(chars)
