WINNING_OUTCOMES = [
    [[1,0,0],[1,0,0],[1,0,0]],
    [[0,1,0],[0,1,0],[0,1,0]],
    [[0,0,1],[0,0,1],[0,0,1]],
    [[1,1,1],[0,0,0],[0,0,0]],
    [[0,0,0],[1,1,1],[0,0,0]],
    [[0,0,0],[0,0,0],[1,1,1]],
    [[1,0,0],[0,1,0],[0,0,1]],
    [[0,0,1],[0,1,0],[1,0,0]]
]
ttt_blocks = [[0,0,0],[0,0,0],[0,0,0]]
sample_ttt_board = [[0,1,0],[0,1,0],[0,1,0]]
has_won = False
for w in WINNING_OUTCOMES:
    if sample_ttt_board == w:
        has_won = True
        break

print (has_won)
# def has_won (blocks, player_num=1):
#     return False    


# ttt_board_splitlines = ttt_board.splitlines()
# i = 0
# for l in ttt_board_splitlines:
#     ttt_board_splitlines[i] = [*l]
#     i += 1
# ttt_board_splitlines[0][0] = "X"

# output = "" 
# for l in ttt_board_splitlines:
#     output += f"{''.join(l)}\n"
# print (output)



