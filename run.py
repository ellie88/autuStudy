"""
------------------------------------
@Time : 2019/9/3 14:21
@Auth : linux超
@File : run.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest
import os


if __name__ == '__main__':
    pytest.main(["-sq",
                 "--alluredir", "./allure-results"])
    os.system(r"allure generate --clean allure-results -o allure-report")