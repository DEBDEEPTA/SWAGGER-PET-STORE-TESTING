from dataclasses import dataclass, field
from datetime import datetime,timezone
@dataclass
class Order:
    id : int
    petId : int
    quantity: int
    shipDate : str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    )
    status: str = "placed"
    complete: bool = False

