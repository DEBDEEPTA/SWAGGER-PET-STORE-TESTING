import os
from datetime import datetime
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):

    if hasattr(config.option, "htmlpath") and config.option.htmlpath:

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        config.option.htmlpath = os.path.join(reports_dir, f"API_Test_Report_{timestamp}.html")
