def tournamentWinner(competitions, results):
    # Write your code here.
    winner = ""
    winner_points = 0
    matches = {}
    for i in range(len(results)):
        print(i)
        if results[i] == 0:
            if not competitions[i][1] in matches:
                matches[competitions[i][1]] = 3
            else:
                matches[competitions[i][1]] += 3
        else:
            if not competitions[i][0] in matches:
                matches[competitions[i][0]] = 3
            else:
                matches[competitions[i][0]] += 3
    print(matches)
    for key in matches:
        # print(key)
        if matches[key] > winner_points:
            winner_points = matches[key]
            winner = key
    return winner

print(tournamentWinner(
    [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ] ,
    [0, 0, 1]
))