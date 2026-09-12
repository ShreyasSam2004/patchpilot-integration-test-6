"""Cancellation refund rules for hotel bookings."""

from decimal import Decimal, ROUND_HALF_UP


def calculate_refund(
    booking_amount: Decimal,
    days_before_checkin: int,
) -> Decimal:
    """Calculate the amount refunded when a booking is cancelled.

    Policy:
    - 7 or more days before check-in: 100% refund
    - 2 through 6 days before check-in: 50% refund
    - Less than 2 days before check-in: no refund
    """
    if booking_amount < 0:
        raise ValueError("booking amount cannot be negative")
    if days_before_checkin < 0:
        raise ValueError("days before check-in cannot be negative")

    if days_before_checkin >= 7:
        refund_rate = Decimal("1.00")
    elif days_before_checkin >= 2:
        refund_rate = Decimal("0.50")
    else:
        refund_rate = Decimal("0.00")

    return (booking_amount * refund_rate).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
