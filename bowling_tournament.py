from bowling import get_score


def tour_winner(input_file, output_file, inter=False):
    with open(input_file, 'r', encoding='utf8') as in_file, \
            open(output_file, 'w', encoding='utf8') as out_file:
        points_name = {}
        for line in in_file:
            line = line.rstrip()
            line_list = line.split()
            if line_list:
                if line_list[0] == '###':
                    out_line = line + '\n'
                    points_name = {}
                elif line_list[0] == 'winner':
                    max_points = max(points_name.keys())
                    winner = points_name[max_points]
                    out_line = f'winner is {winner}\n'
                else:
                    result = get_score(line_list[1], inter=inter)
                    out_line = f'{line} {result}\n'
                    if isinstance(result, int):
                        points_name[result] = line_list[0]
            else:
                out_line = '\n'
            out_file.write(out_line)
