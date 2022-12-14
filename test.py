import unittest

from unittest.mock import patch
from first_task import get_score, get_offset
# Для разработанной в предыдущем задании функции get_score(game_stamps, offset)
# разработайте unit-тесты на фреймворке unittest.
# Тесты должны учитывать все возможные случаи использования функции,
# концентрироваться на проверке одного случая, не повторяться,
# название тестов должно отражать суть выполняемой проверки.


class TestMethods(unittest.TestCase):
    game_stamps_values = [{'offset': 99850, 'score': {'away': 3, 'home': 6}},
                          {'offset': 99853, 'score': {'away': 3, 'home': 6}},
                          {'offset': 99854, 'score': {'away': 3, 'home': 6}},
                          {'offset': 99857, 'score': {}},
                          {'offset': 99860, 'score': {'home': 6}},
                          {'offset': 99863, 'score': {'away': 3}}]

    def test_offset_in_game_stamps(self):
        """Testing common function cases"""
        test_score = get_score(self.game_stamps_values, 99850)
        self.assertEqual(test_score, {'offset': 99850, 'score': {'home': 6, 'away': 3}})

    def test_no_offset_in_game_stamps(self):
        """Testing cases when there's no such offset in game stamps"""
        test_score = get_score(self.game_stamps_values, 99900)
        self.assertEqual(test_score, "Game stamps list doesn't content such offset value!")

    def test_no_score(self):
        """Testing cases when offset game stamp contains no score"""
        test_score = get_score(self.game_stamps_values, 99857)
        self.assertEqual(test_score, {'offset': 99857, 'score': {'home': 0, 'away': 0}})

    def test_none_home_or_away_score(self):
        """Testing cases when 'home' or 'away' is empty"""
        test_score = get_score(self.game_stamps_values, 99860)
        self.assertEqual(test_score, {'offset': 99860, 'score': {'home': 6, 'away': 0}})
        test_score = get_score(self.game_stamps_values, 99863)
        self.assertEqual(test_score, {'offset': 99863, 'score': {'home': 0, 'away': 3}})

    @patch('builtins.input', lambda _: 'cow')
    def test_wrong_offset_input(self):
        """Testing cases when offset gets string values instead of int """
        with self.assertRaises(ValueError):
            offset = int(input('Please, type in the target offset: '))
            assert get_offset() == 'cow'


if __name__ == '__main__':
    unittest.main()
