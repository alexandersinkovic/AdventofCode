from aoc_fetcher import get_data

input = get_data(2021, 21)

def part1():
    data = input.strip().splitlines()

    player1_position = int(data[0][-1:]) -1
    player2_position = int(data[1][-1:]) -1

    player1_score = 0
    player2_score = 0

    die = 0
    rolls = 0

    losing_score = 0

    while(True):
        player1_position = (player1_position + (((die + 1)*3 + 3) % 10)) % 10
        rolls += 3
        die = (die + 3) % 10
        player1_score += player1_position + 1
        if player1_score >= 1000:
            losing_score = player2_score
            break
        player2_position = (player2_position + (((die + 1)*3 + 3) % 10)) % 10
        rolls += 3
        die = (die + 3) % 10
        player2_score += player2_position + 1
        if player2_score >= 1000:
            losing_score = player1_score
            break


    print(rolls * losing_score)


def part2():
    data = input.strip().splitlines()

    player1_position = int(data[0][-1:]) -1
    player2_position = int(data[1][-1:]) -1

    player1_score = 0
    player1_wins = 0
    player2_score = 0
    player2_wins = 0

    is_player_1 = True

    die_rolls = [1,3,6,7,6,3,1]

    wins1, wins2 = play(True,player1_position, player2_position, player1_score, player2_score, player1_wins, player2_wins, 1, die_rolls)

    print(wins1)
    print(wins2)

def play(is_player_1, pos1, pos2, score1, score2, wins1, wins2, universes, die_rolls):
    if is_player_1:
        #print("player1 plays", pos1, pos2, score1, score2, wins1, wins2, universes)
        for idx, num_universe in enumerate(die_rolls):
            #print("for-loop")
            #print(pos1, idx)
            new_pos = (pos1 + idx + 3) % 10
            #print("New_Pos:", new_pos)
            new_score = score1 + new_pos + 1
            #print(universes, num_universe)
            new_universes = universes * num_universe
            #print(new_universes)
            if new_score >= 21:
                wins1 = wins1 + new_universes
            else:
                wins1, wins2 = play(False, new_pos, pos2, new_score, score2, wins1, wins2, new_universes, die_rolls)
        return wins1, wins2

    else:
        #print("player2 plays", pos1, pos2, score1, score2, wins1, wins2, universes)
        for idx, num_universe in enumerate(die_rolls):
            new_pos = (pos2 + idx + 3) % 10
            new_score = score2 + new_pos + 1
            new_universes = universes * num_universe
            if new_score >= 21:
                wins2 = wins2 + new_universes
            else:
                wins1, wins2 = play(True, pos1, new_pos, score1, new_score, wins1, wins2, new_universes, die_rolls)
        return wins1, wins2


part2()
