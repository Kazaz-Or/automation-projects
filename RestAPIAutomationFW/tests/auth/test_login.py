from RestAPIAutomationFW.lib.auth import Auth
from RestAPIAutomationFW.config import APP_URL, LOG, ADMIN_USER, ADMIN_PASSWORD


def test_login():
    LOG.info("test_login")
    response = Auth().login(APP_URL, ADMIN_USER, ADMIN_PASSWORD)
    LOG.debug(response.json())
    assert response.status_code == 200
