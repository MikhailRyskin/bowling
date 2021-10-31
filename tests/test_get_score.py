import unittest
from lesson_014.bowling import get_score, check_game_result, check_frame, StrikeError, SpareError


class GetScoreTest(unittest.TestCase):
    def test_strike(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, 200, 'не работает подсчёт strike')

    def test_spare(self):
        result = get_score('4/3/2/5/9/1/8/5/5/3/')
        self.assertEqual(result, 150, 'не работает подсчёт spare')

    def test_0first(self):
        result = get_score('-4-3-2-1---8-1-4-3--')
        self.assertEqual(result, 26, 'не работает подсчёт первая 0 очков')

    def test_points69(self):
        result = get_score('443322517-188154533-')
        self.assertEqual(result, 69, 'не работает подсчёт две попытки с очками')

    def test_points63(self):
        result = get_score('81716151414333221154')
        self.assertEqual(result, 63, 'не работает подсчёт две попытки с очками')

    def test_points122(self):
        result = get_score('Х4/34-48/45173/X18')
        self.assertEqual(result, 122, 'не работает подсчёт разные результаты')

    def test_points0(self):
        result = get_score('--------------------')
        self.assertEqual(result, 0, 'не работает подсчёт все промахи')

    def test_not10frames_error(self):
        result = get_score('XXX')
        self.assertEqual(result, 'результат должен содержать 10 фреймов',
                         'не замечает неверное количество фреймов')

    def test_value_error(self):
        result = get_score('Х4/34-48/451f3/X18')
        self.assertEqual(result, 'недопустимый символ в результате: f',
                         'не замечает недопустимый символ')

    def test_attribute_error(self):
        result = get_score('Х4/94-48/45173/X18')
        self.assertEqual(result, 'сумма позиций фрейма больше 9: 94',
                         'не замечает сумму позиций больше 9')

    def test_spare_error(self):
        result = get_score('Х/494-48/45173/X18')
        self.assertEqual(result, 'символ spare на первой позиции в результате фрейма: /4',
                         'не замечает spire на 1 позиции')

    def test_strike_error(self):
        result = get_score('X18X8/-47X/5/1854')
        self.assertEqual(result, 'символ strike на второй позиции в результате фрейма: 7X',
                         'не замечает strike на 2 позиции')

    def test_value_error1(self):
        self.assertRaises(ValueError, check_game_result, 'rrrrrrrrrrrrrrrrrrrr')

    def test_strike_error1(self):
        self.assertRaises(StrikeError, check_game_result, 'X18X8/-47X/5/1854')

    def test_spare_error1(self):
        self.assertRaises(SpareError, check_frame, '/', '8')

    def test_inter_points146(self):
        result = get_score('XXX347/21-1XX3/', inter=True)
        self.assertEqual(result, 146, 'не работает подсчёт разные результаты')

    def test_inter_points75(self):
        result = get_score('-1-1-1-1-1XXX1212', inter=True)
        self.assertEqual(result, 75, 'не работает подсчёт разные результаты')


if __name__ == '__main__':
    unittest.main()
