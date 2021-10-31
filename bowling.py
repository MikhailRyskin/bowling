class Not10FramesError(Exception):
    def __str__(self):
        return 'результат должен содержать 10 фреймов'


class SpareError(Exception):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f'символ spare на первой позиции в результате фрейма: {self.first}{self.second}'


class StrikeError(Exception):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f'символ strike на второй позиции в результате фрейма: {self.first}{self.second}'


def get_score(game_result, inter=False):
    game_result = game_result.replace('Х', 'X')
    mod_result = character_replacement(game_result)
    try:
        check_game_result(game_result)
        check_mod_result(mod_result)
        if inter:
            total_points = scoring_inter(mod_result)
        else:
            total_points = scoring(mod_result)
        print(f'Количество очков для результатов {game_result}: {total_points}')
        return total_points
    except (Not10FramesError, ValueError, AttributeError, SpareError, StrikeError) as exp:
        print(exp)
        return str(exp)


def scoring(mod_result):
    total_points = 0
    poz = 0
    while poz < len(mod_result) - 1:
        first, second = mod_result[poz], mod_result[poz + 1]
        check_frame(first, second)
        if first == 'X':
            points = 20
        elif second == '/':
            points = 15
        else:
            points = int(first) + int(second)
        total_points += points
        poz += 2
    return total_points


def scoring_inter(mod_result):
    check_all_frames(mod_result)
    total_points = 0
    poz = 0
    not_last = True
    not_penult = True
    while poz < len(mod_result) - 1:
        first, second = mod_result[poz], mod_result[poz + 1]
        if first == 'X':
            points = strike_points_inter(mod_result, not_last, not_penult, poz)
        elif second == '/':
            points = spare_points_inter(mod_result, not_last, poz)
        else:
            points = int(first) + int(second)
        total_points += points
        poz += 2
        if poz == len(mod_result) - 4:
            not_penult = False
        if poz == len(mod_result) - 2:
            not_last = False
    return total_points


def spare_points_inter(mod_result, not_last, poz):
    points = 10
    if not_last:
        if mod_result[poz + 2] == 'X':
            points += 10
        else:
            points += int(mod_result[poz + 2])
    return points


def strike_points_inter(mod_result, not_last, not_penult, poz):
    points = 10
    if not_last:
        if mod_result[poz + 2] == 'X':
            points += 10
            if not_penult:
                if mod_result[poz + 4] == 'X':
                    points += 10
                else:
                    points += int(mod_result[poz + 4])
        else:
            if mod_result[poz + 3] == '/':
                points += 10
            else:
                points += int(mod_result[poz + 2]) + int(mod_result[poz + 3])
    return points


def character_replacement(result):
    modified_result = ''
    for symbol in result:
        if symbol == 'X':
            modified_result += 'X0'
        elif symbol == '-':
            modified_result += '0'
        else:
            modified_result += symbol
    return modified_result


def check_game_result(res):
    valid_characters = '123456789-/X'
    for char in res:
        if char not in valid_characters:
            raise ValueError(f'недопустимый символ в результате: {char}')
    was_already = 0
    check_line = list(res)
    number_of_x = check_line.count('X')
    for _ in range(number_of_x):
        strike_index = check_line.index('X')
        check_index = was_already + strike_index
        if check_index % 2 != 0:
            raise StrikeError(res[strike_index - 1], res[strike_index])
        was_already += 1
        check_line[strike_index] = 0


def check_mod_result(res):
    if len(res) != 20:
        raise Not10FramesError()


def check_frame(first_char, second_char):
    if first_char == '/':
        raise SpareError(first_char, second_char)
    elif first_char.isdigit() and second_char.isdigit():
        if int(first_char) + int(second_char) > 9:
            raise AttributeError(f'сумма позиций фрейма больше 9: {first_char}{second_char}')


def check_all_frames(mod_result):
    poz = 0
    while poz < len(mod_result) - 1:
        first, second = mod_result[poz], mod_result[poz + 1]
        check_frame(first, second)
        poz += 2
