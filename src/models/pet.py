from dataclasses import  dataclass
from src.models.category import Category
from src.models.tags import Tag
from typing import List
@dataclass
class Pet:
    id :int
    category: Category
    name : str
    photoUrls : List[str]
    tags :List[Tag]
    status: str
