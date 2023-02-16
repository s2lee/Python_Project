from contextlib import ContextDecorator
from unittest.mock import patch, DEFAULT
import path
from context_managers import handle_calorie_decorator, work


def _patch_deps():
    return patch.multiple(
        "context_managers", have_breakfast=DEFAULT, exercise_hard=DEFAULT
    )


def test_cm_calls_functions():
    with _patch_deps() as deps:
        with handle_calorie_decorator() as calorie_handle:
            handler_class = calorie_handle.__class__
            assert issubclass(handler_class, ContextDecorator) == True

        deps["have_breakfast"].assert_called_once_with()
        deps["exercise_hard"].assert_called_once_with()


def test_cm_autocalled():
    with _patch_deps() as deps:
        work()

        deps["have_breakfast"].assert_called_once_with()
        deps["exercise_hard"].assert_called_once_with()
