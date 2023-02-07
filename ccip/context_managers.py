import contextlib


def have_breakfast():
    print("Breakfast replenishes the stores of energy and nutrients in your body")


def exercise_hard():
    print(
        "Physical activity stimulates various brain chemicals that may leave you feeling happier"
    )


def work_hard():
    print("When working hard for something, this thing becomes part of us in some way")


# 1
class CalorieHandler:
    def __enter__(self):
        have_breakfast()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        exercise_hard()


# 2
@contextlib.contextmanager
def handler_calorie():
    try:
        have_breakfast()
        yield
    finally:
        exercise_hard()


# 3
class handler_calorie_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        have_breakfast()
        return self

    def __exit__(self, ext_type, ex_value, ex_traceback):
        exercise_hard()


@handler_calorie_decorator()
def work():
    print("When working hard for something, this thing becomes part of us in some way")


def main():
    with CalorieHandler():
        work_hard()

    with handler_calorie():
        work_hard()

    work()


if __name__ == "__main__":
    main()
