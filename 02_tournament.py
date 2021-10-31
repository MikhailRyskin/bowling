# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обработки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>

#
import argparse
from bowling_tournament import tour_winner

parser = argparse.ArgumentParser(description='Консольный скрипт для формирования файла с результатами турнира.')
parser.add_argument('--input', '-input', type=str, default='tournament.txt',
                    help='файл протокол турнира. По умолчанию: tournament.txt')
parser.add_argument('--output', '-output', type=str, default='tournament_result.txt',
                    help='файл c результатами турнира. По умолчанию: tournament_result.txt')
parser.add_argument('--inter', '-inter', type=str, default=False, help='Система подсчёта очков: по умолчанию - '
                                                                       'российская, True - международная')
args = parser.parse_args()
try:
    tour_winner(input_file=args.input, output_file=args.output, inter=args.inter)
except FileNotFoundError:
    print(f'файла протокола турнира {args.input} не существует')

# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+

# зачет!