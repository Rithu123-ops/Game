def full_form(x):
    if x == "r":
        return "Rock"
    if x == "s":
        return "Scissors"
    if x == "p":
        return "Paper"


def user_error(y):
    if y in ['r', 'p', 's']:
        return True
    else:
        return False


def play(store_his):
    while True:
        user_1 = str(input("user 1 turn, choose r for rock, p for paper, s for scissors : \n")).lower()
        if user_error(user_1):
            while True:
                user_2 = str(input("User 2 turn, choose r for rock, p for paper, s for scissors : \n")).lower()
                if user_error(user_2):
                    break
                else:
                    print("invalid input please enter the correct input:")
            break
        else:
            print("invalid input please enter the correct input:")

    store_his["user_1"].append(user_1)
    store_his["user_2"].append(user_2)

    def winner(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
                player == 'p' and opponent == 'r'):
            return True

    if user_1 == user_2:
        store_his['result'].append("Tie")

    else:
        if winner(user_1, user_2):
            store_his["user_1_point"] += 1
            store_his["result"].append("User_1 Won")
        else:
            store_his["user_2_point"] += 1
            store_his["result"].append("User_2 Won")

    return store_his


game_round = 1
store_history = {"user_1": [], 'user_1_point': 0, "user_2": [], 'user_2_point': 0, "result": []}

while game_round <= 5:
    print(f"Round {game_round}")
    store_history = play(store_history)
    game_round += 1
if store_history["user_1_point"] == store_history["user_2_point"]:
    print(f"both get same point {store_history['user_1_point']}")

else:
    if store_history["user_1_point"] > store_history["user_2_point"]:
        print(
            f"\nUser_1 has {store_history['user_1_point']} points User_2 has {store_history['user_2_point']} points, "
            f"\nHence User_1 "
            f"Won the Game.\n")


    else:
        print(
            f"\nUser_1 has {store_history['user_1_point']} points User_2 has {store_history['user_2_point']} points, "
            f"\nHence User_2 "
            f"Won the Game.\n")

while True:
    try:
        details = int(input("Do you want to know information about any round :"))
        round_info_user = full_form(store_history["user_1"][details - 1])
        print(f"\nUser_1 choose {round_info_user}")
        round_info_comp = full_form(store_history["user_2"][details - 1])
        print(f"User_2 choose {round_info_comp}")
        print(store_history["result"][details - 1])
        break

    except:
        print("please choose correct round.")
