letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters]
points *= 2
letters_to_points = {key:value for key, value in zip(letters, points)}
letters_to_points[" "] = 0
print("Here are the assigned points for each letters: ", letters_to_points)

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letters_to_points.get(letter, 0)
    return point_total

brownie_points = score_word("BROWNIE")
print("Points scored for playing word \"BROWNIE\":", brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],"wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER" ,"BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

update_point_totals()
print("Points scored by each players round1:", player_to_points)

def play_word(player, word):
    player_to_words[player].append(word)
    update_point_totals()

play_word("player1", "CODE")
play_word("wordNerd", "SPORT")
play_word("Lexi Con", "LOVE")
play_word("Prof Reader", "GAME")
print("Words played by players in round2:", player_to_words)
print("Points scored by each players round2:", player_to_points)

play_word("player1", "cooking")
print(player_to_words)
print(player_to_points)









