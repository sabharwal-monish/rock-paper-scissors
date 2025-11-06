from collections import Counter

def player(prev_play):
    if prev_play == "":
        player.my_history = []
        player.opp_history = []
        player.opponent_type = None

    if not hasattr(player, "my_history"):
        player.my_history = []
        player.opp_history = []
        player.opponent_type = None

    if prev_play:
        player.opp_history.append(prev_play)

    def beat(m): return {"R":"P","P":"S","S":"R"}[m]

    hist_len = len(player.my_history)

    if hist_len < 5:
        opening = ["R", "P", "S", "P", "R"]
        move = opening[hist_len]
        player.my_history.append(move)
        return move

    if player.opponent_type is None and hist_len >= 5:
        quincy_pattern = ["R", "R", "P", "P", "S"]
        quincy_match = sum(1 for i in range(len(player.opp_history)) 
                          if player.opp_history[i] == quincy_pattern[(i+1) % 5])
        
        kris_match = 0
        for i in range(1, len(player.opp_history)):
            if player.opp_history[i] == beat(player.my_history[i-1]):
                kris_match += 1
        
        if quincy_match >= 4:
            player.opponent_type = "quincy"
        elif kris_match >= 3:
            player.opponent_type = "kris"
        else:
            player.opponent_type = "abbey_or_mrugesh"

    if player.opponent_type == "quincy":
        quincy_pattern = ["R", "R", "P", "P", "S"]
        next_quincy_move = quincy_pattern[(len(player.opp_history) + 1) % 5]
        move = beat(next_quincy_move)
        player.my_history.append(move)
        return move

    if player.opponent_type == "kris":
        last_move = player.my_history[-1]
        move = beat(beat(last_move))
        player.my_history.append(move)
        return move

    if player.opponent_type == "abbey_or_mrugesh":
        if hist_len >= 10:
            last10 = player.my_history[-10:]
            most_common = Counter(last10).most_common(1)[0][0]
            predicted_move = beat(most_common)
            move = beat(predicted_move)
            player.my_history.append(move)
            return move
        else:
            move = "P"
            player.my_history.append(move)
            return move

    move = "P"
    player.my_history.append(move)
    return move
