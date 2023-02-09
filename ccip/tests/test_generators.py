import pytest
import path

from generators import SalesOrderStats


def test_calculations():
    stats = SalesOrderStats(range(1, 25 + 1)).process()

    assert stats.min_order_price == 1
    assert stats.max_order_price == 25
    assert stats.avg_price == 13


def test_empty():
    with pytest.raises(ValueError):
        SalesOrderStats([])
