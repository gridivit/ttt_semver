"""Pytest conftest."""
import os

import pytest

pytest_plugins = [
    "subs_qa_automation.plugins.pytest_return_code",

    "subs_qa_automation.fixtures.common_fixtures",
]


def pytest_addoption(parser: pytest.Parser):
    """Adds extra parameters for pytest."""
    parser.getgroup("subs").addoption(
        "--subs-host",
        action="store",
        default=os.environ.get('SUBS_HOST'),
        help="Subs stand host"
    )
    parser.getgroup("subs").addoption(
        "--subs-api-token",
        action="store",
        default=os.environ.get('SUBS_API_TOKEN'),
        help="Subs api token"
    )
