from blocked_users import blocked_users


def is_blocked(user_id):
    left, right = 0, len(blocked_users) - 1

    while left <= right:
        mid = (left + right) // 2

        if blocked_users[mid] == user_id:
            return True
        if blocked_users[mid] < user_id:
            left = mid + 1
        else:
            right = mid - 1

    return False


user_id = int(input("შეიყვანე იუზერის ID: "))

if is_blocked(user_id):
    print(f"იუზერი {user_id} დაბლოკილია")
else:
    print(f"იუზერი {user_id} არ არის დაბლოკილი")