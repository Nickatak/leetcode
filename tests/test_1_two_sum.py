import importlib

import pytest


@pytest.mark.parametrize(
    "nums,target,expected",
    [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])],
)
def test_1_two_sum(runner, nums, target, expected):
    problem = importlib.import_module("problems.1_two_sum")
    assert runner.run(problem.Solution, nums, target) == expected
