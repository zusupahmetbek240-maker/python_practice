raw_users = ["  alex_99 ", "ADMIN", "  john_doe  ", "admin", "  guest_01 ", "ADMIN "]
clean_users = list((usr.strip().lower() for usr in raw_users if usr.strip().lower() != "admin"))
print(clean_users)

grades = [("Алихан", 85), ("Дильназ", 90), ("Алихан", 95), ("Арман", 78), ("Дильназ", 88)]
board = {}
for pi, points in grades:
    board.setdefault(pi, []).append(points)
print(board)