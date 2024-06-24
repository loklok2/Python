def find_num(input_str):
    if input_str in ['A', 'B', 'C']:
        return 2
    elif input_str in['D', 'E', 'F']:
        return 3
    elif input_str in['G', 'H', 'I']:
        return 4
    elif input_str in['J', 'K', 'L']:
        return 5
    elif input_str in['M', 'N', 'O']:
        return 6
    elif input_str in['P', 'Q', 'R', 'S']:
        return 7
    elif input_str in['T', 'U', 'V']:
        return 8
    elif input_str in['W', 'X', 'Y', 'Z']:
        return 9
    else:
        return input_str
    