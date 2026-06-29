players = []
n = int(input("Enter number of players: "))

for i in range(n):
    name = input("Enter player name: ")
    players.append(name)

players.sort()

print("\nPlayers sorted alphabetically:")
for p in players:
    print("-", p)
