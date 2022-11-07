import pytest


class TestStorm(object):
    @pytest.mark.L1
    def test_001(self):
        a = 3
        assert a == 4
        print("断言失败！")
    @pytest.mark.L2
    def test_002(self):
        a = 3
        assert a == 3
        print("断言成功！")


if __name__ == '__main__':
    # pytest.main(["-s", "test_01.py", "--html=report1.html"])
    pytest.main(["-s", "test_01.py", "-m", "L1", "--alluredir=./report"])

