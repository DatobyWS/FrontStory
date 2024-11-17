from dataclasses import dataclass
from datetime import datetime

@dataclass
class Campaign:
    campaign_id: int
    name: str
    date: datetime
    revenue: float
    cost: float
    clicks: int

    @property
    def profit(self) -> float:
        return self.revenue - self.cost

    @property
    def cpc(self) -> float:
        return self.cost / self.clicks if self.clicks else 0

    @property
    def roi(self) -> float:
        return (self.revenue / self.cost) if self.cost else 0
