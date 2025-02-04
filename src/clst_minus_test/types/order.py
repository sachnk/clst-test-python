# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Order"]


class Order(BaseModel):
    account_id: str
    """Account ID for the account."""

    created_at: int
    """When the order was created in milliseconds since epoch."""

    filled_quantity: str
    """The quantity that has been filled."""

    order_id: str
    """An internally generated unique ID for this order."""

    order_type: Literal["limit", "market"]
    """The type of order, can be one of the following:

    - `limit`: A limit order will execute at-or-better than the limit price you
      specify
    - `market`: An order that will execute at the prevailing market prices
    """

    quantity: str
    """The requested quantity on this order."""

    side: Literal["buy", "sell", "sell-short"]
    """Buy, sell, sell-short indicator."""

    state: Literal["open", "rejected", "closed"]
    """Simplified order state, which is inferred from `OrderStatus`.

    Makes it easier to determine whether an order can be executed against.

    - `open`: Order _can_ potentially be executed against.
    - `rejected`: Order _cannot_ be executed against because it was rejected. This
      is a terminal state.
    - `closed`: Order _cannot_ be executed against. This is a terminal state.
    """

    status: Literal[
        "new",
        "partially-filled",
        "filled",
        "canceled",
        "replaced",
        "pending-cancel",
        "stopped",
        "rejected",
        "suspended",
        "pending-new",
        "calculated",
        "expired",
        "accepted-for-bidding",
        "pending-replace",
        "done-for-day",
    ]
    """
    Granular order status using
    [standard values come FIX tag 39](https://www.fixtrading.org/online-specification/order-state-changes).
    """

    strategy_type: Literal["sor", "dark", "ap", "pov", "twap", "vwap"]
    """Strategy type used for execution, can be one of below.

    Note, we use sensible defaults for strategy parameters at the moment. In future,
    we will provide a way to provide specify these parameters.

    - `sor`: Smart order router
    - `dark`: Dark pool
    - `ap`: Arrival price
    - `pov`: Percentage of volume
    - `twap`: Time weighted average price
    - `vwap`: Volume weighted average price

    For more information on these strategies, please refer to our
    [documentation](https://docs.clearstreet.io/studio/docs/execution-strategies).
    """

    symbol: str

    time_in_force: Literal["day", "ioc", "day-plus", "at-open", "at-close"]
    """The lifecycle enforcement of this order.

    - `day`: The order will exist for the duration of the current trading session
    - `ioc`: The order will immediately be executed or cancelled
    - `day-plus`: The order will exist only for the duration the current trading
      session plus extended hours, if applicable
    - `at-open`: The order will exist only for the opening auction of the next
      session
    - `at-close`: The order will exist only for the closing auction of the current
      session
    """

    updated_at: int
    """When the order was updated in milliseconds since epoch."""

    version: int
    """A monotonically increasing number indicating the version of this order.

    A higher number indicates a more recent version of the order.
    """

    average_price: Optional[float] = None
    """Calculated average price of all fills on this order."""

    order_update_reason: Optional[Literal["place", "modify", "cancel", "execution-report", "cancel-reject"]] = None
    """The last reason why this order was updated"""

    price: Optional[str] = None
    """The requsted limit price on this order."""

    reference_id: Optional[str] = None
    """The ID you provided when creating this order."""

    text: Optional[str] = None
    """Free form text typically contains reasons for a reject."""
