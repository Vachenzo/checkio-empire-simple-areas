from checkio_referee import RefereeBase
from checkio_referee import covercodes
from checkio_referee.util import validators

import settings
import settings_env
from tests import TESTS

Validator = validators.FloatEqualValidator

Validator.PRECISION = 2

class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "simple_areas"
    VALIDATOR = Validator
    ENV_COVERCODE = {
        "python_2": covercodes.py_unwrap_args,
        "python_3": covercodes.py_unwrap_args,
        "javascript": None
    }
