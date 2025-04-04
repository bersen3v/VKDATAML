from dataclasses import dataclass, field
import uuid

@dataclass
class Customer:
    login: str
    password: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)