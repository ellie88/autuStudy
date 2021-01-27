"""
------------------------------------
@Time : 2019/8/28 19:50
@Auth : linux超
@File : conftest.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest
import allure



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


@allure.step("打开浏览器")
def fixture_step():
    pass


@pytest.fixture
def init_url():
    fixture_step()
    yield True