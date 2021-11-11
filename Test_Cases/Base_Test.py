import pytest


@pytest.mark.usefixtures("log_on_failure", "get_browser")
class BaseTest:
    pass
