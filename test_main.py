# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

import pytest

if __name__ == '__main__':
   os.system('pytest --alluredir ./report/allure_report --clean-alluredir')
   os.system('allure serve report/allure_report')
