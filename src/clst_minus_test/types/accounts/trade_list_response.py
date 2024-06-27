# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..trade import Trade
from ..._models import BaseModel

__all__ = ["TradeListResponse"]


class TradeListResponse(BaseModel):
    data: List[Trade]

    next_page_token: Optional[str] = None
    """Cursor for the next page of results."""
