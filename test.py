import unittest
from first_task import *
# Для разработанной в предыдущем задании функции get_score(game_stamps, offset)
# разработайте unit-тесты на фреймворке unittest.
# Тесты должны учитывать все возможные случаи использования функции,
# концентрироваться на проверке одного случая, не повторяться,
# название тестов должно отражать суть выполняемой проверки.


class TestMethods(unittest.TestCase):
    def test_offset_in_game_stamps(self):
        pass

    def test_no_offset_in_game_stamps(self):
        pass

    def test_no_score(self):
        pass

    def test_no_home_or_away_score(self):
        pass


if __name__ == '__main__':
    unittest.main()
