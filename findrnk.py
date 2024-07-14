def findRelativeRanks(score):
  sorted_score = sorted(score, reverse=True)
  rank_map = {}
  for i in range(len(sorted_score)):
    if i == 0:
      rank_map[sorted_score[i]] = "Gold Medal"
    elif i == 1:
      rank_map[sorted_score[i]] = "Silver Medal"
    elif i == 2:
      rank_map[sorted_score[i]] = "Bronze Medal"
    else:
      rank_map[sorted_score[i]] = str(i + 1)

  ranks = []
  for s in score:
    ranks.append(rank_map[s])

  return ranks

score = [5, 4, 3, 2, 1]
ranks = findRelativeRanks(score)
print(ranks)
