from typing import List
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


class PersonIntel(BaseModel):
    summary: str = Field(description="A short summary about the person")
    facts: list = Field(description="Interesting facts about the person")
    topics_of_interest: List[str] = Field(
        description="Topics of interest of the person")
    ice_breakers: List[str] = Field(
        description="Ice breakers to start a conversation with the person")

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers
        }
        
person_intel_parser:PydanticOutputParser = PydanticOutputParser(pydantic_object=PersonIntel)
