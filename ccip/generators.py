class SalesOrderStats:
    def __init__(self, sales):
        self.sales = iter(sales)
        self.min_order_price: float = None
        self.max_order_price: float = None
        self._total_sales_price: float = 0.0
        self._total_sales = 0
        self._initialize()

    def _initialize(self):
        try:
            first_value = next(self.sales)
        except StopIteration:
            raise ValueError("no values provided")

        self.min_order_price = self.max_order_price = first_value
        self._update_avg(first_value)

    def process(self):
        for sale_value in self.sales:
            self._update_min(sale_value)
            self._update_max(sale_value)
            self._update_avg(sale_value)
        return self

    def _update_min(self, new_value: float):
        if new_value < self.min_order_price:
            self.min_order_price = new_value

    def _update_max(self, new_value: float):
        if new_value > self.max_order_price:
            self.max_order_price = new_value

    @property
    def avg_price(self):
        return self._total_sales_price / self._total_sales

    def _update_avg(self, new_value: float):
        self._total_sales_price += new_value
        self._total_sales += 1

    def __str__(self):
        return (
            f"{self.__class__.__name__}({self.min_order_price}, "
            f"{self.max_order_price}, {self.avg_price})"
        )


def _load_sales(sales_data):
    sales = []
    with open(sales_data) as f:
        for line in f:
            *_, price_raw = line.partition(",")
            sales.append(float(price_raw))

    return sales


def load_sales(sales_data):
    with open(sales_data) as f:
        for line in f:
            *_, price_raw = line.partition(",")
            yield float(price_raw)


def main():
    SALES_FILE = None
    sales = load_sales(SALES_FILE)
    stats = SalesOrderStats(sales).process()
    print(stats)


if __name__ == "__main__":
    main()
