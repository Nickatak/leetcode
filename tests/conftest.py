import pathlib
import sys
from typing import Generator

import pytest

# Unfortunately, this needs to happen first.
test_dir = pathlib.Path(__file__).parent

sys.path.append(str(test_dir.parent.absolute()))


@pytest.fixture
def runner() -> Generator:
    yield MultipleSolutionRunner()


class MultipleSolutionRunner:

    def run(self, SolutionClass, *args, **kwargs):
        SolutionInstance = SolutionClass()
        methods_list = [
            getattr(SolutionInstance, m)
            for m in dir(SolutionClass)
            if callable(getattr(SolutionClass, m)) and not m.startswith("__")
        ]
        answer = methods_list.pop()(*args, **kwargs)

        for method in methods_list:
            # ERROR: All solutions must have the same answer, otherwise we know something is definitely incorrect.
            assert method(*args, **kwargs) == answer

        return answer
