# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorerOne = "Ruud Gullit"
scorerTwo = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = scorerOne + " " + str(goal_0) + ", " + scorerTwo + " " + str(goal_1)
report = f"{scorerOne} scored in the {goal_0}nd minute\n{scorerTwo} scored in the {goal_1}th minute"
player = "Erwin Koeman"
first_name = player[0:player.find(" "):1]
last_name = player[player.find(" ")+1:len(player):1]
last_name_len = len(last_name)
name_short = f"{player[0:1]}. {last_name}"
temp_chant = f"{first_name}! " * 5
chant = temp_chant[0: len(temp_chant)-1]
good_chant = chant[len(chant)-1] != " "
