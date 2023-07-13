from dataclasses import dataclass, field
from typing import List


@dataclass
class ImageClasses:
    filename: str
    classes: List[str] = field(default_factory=lambda: [])
