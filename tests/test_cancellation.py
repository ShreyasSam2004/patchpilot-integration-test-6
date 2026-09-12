from decimal import Decimal

import pytest

from booking.cancellation import calculate_refund


def test_cancellation_well_before_checkin_gets_full_refund():
    assert calculate_refund(Decimal("1200.00"), 10) == Decimal("1200.00")


def test_cancellation_exactly_seven_days_before_gets_full_refund():
    assert calculate_refund(Decimal("1200.00"), 7) == Decimal("1200.00")


def test_cancellation_six_days_before_gets_half_refund():
    assert calculate_refund(Decimal("1200.00"), 6) == Decimal("600.00")


def test_cancellation_two_days_before_gets_half_refund():
    assert calculate_refund(Decimal("1200.00"), 2) == Decimal("600.00")


def test_cancellation_three_days_before_gets_half_refund():
    assert calculate_refund(Decimal("1200.00"), 3) == Decimal("600.00")


def test_last_minute_cancellation_gets_no_refund():
    assert calculate_refund(Decimal("1200.00"), 1) == Decimal("0.00")


def test_negative_booking_amount_is_rejected():
    with pytest.raises(ValueError, match="booking amount"):
        calculate_refund(Decimal("-10.00"), 5)


def test_negative_days_are_rejected():
    with pytest.raises(ValueError, match="days before check-in"):
        calculate_refund(Decimal("100.00"), -1)
