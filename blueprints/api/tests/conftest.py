import os.path

import pytest

import main


@pytest.fixture(scope='function')
def app_instance():
    app = main.app
    app.config["DATA_PATH_POSTS"] = os.path.join("tests", "post_mock")
    test_client = app.test_client()
    return test_client
