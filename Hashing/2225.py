"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

Approach 1: HashSet
Time Complexity = O(n log n)
Space Complexity = O(n)
"""

def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    zero_loss = set()
    one_loss = set()
    more_losses = set()

    for winner, loser in matches:
        if (winner not in one_loss) and (winner not in more_losses):
            zero_loss.add(winner)
        if loser in zero_loss:
            zero_loss.remove(loser)
            one_loss.add(loser)
        elif loser in one_loss:
            one_loss.remove(loser)
            more_losses.add(loser)
        elif loser in more_losses:
            continue
        else:
            one_loss.add(loser)
    
    return [sorted(list(zero_loss)), sorted(list(one_loss))]


"""
Approach 2: HashMap + HashSet
Time Complexity = O(n log n)
Space Complexity = O(n)
"""

def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    seen = set()
    losses_count = defaultdict(int)

    for winner, loser in matches:
        seen.add(winner)
        seen.add(loser)
        losses_count[loser] += 1
    
    zero_loss = []
    one_loss = []
    for player in seen:
        count = losses_count.get(player)
        if count == 0:
            zero_loss.append(player)
        elif count == 1:
            one_loss.append(player)

    return [sorted(zero_loss), sorted(one_loss)]

"""
Approach 3: HashMap
Time Complexity = O(n log n)
Space Complexity = O(n)
"""

def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    losses_count = defaultdict(int)

    for winner, loser in matches:
        losses_count[winner] += 0
        losses_count[loser] += 1
    
    zero_loss = []
    one_loss = []
    for player, count in losses_count.items():
        if count == 0:
            zero_loss.append(player)
        elif count == 1:
            one_loss.append(player)

    return [sorted(zero_loss), sorted(one_loss)]

"""
Approach 4: Counting with Array
Time Complexity = O(n + k)
Space Complexity = O(k)
"""

def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    losses_count = [-1] * 100001

    for winner, loser in matches:
        if losses_count[winner] == -1:
            losses_count[winner] = 0
        if losses_count[loser] == -1:
            losses_count[loser] = 1
        else:
            losses_count[loser] += 1
    
    ans = [[], []]
    for i in range(100001):
        if losses_count[i] == 0:
            ans[0].append(i)
        elif losses_count[i] == 1:
            ans[1].append(i)
    
    return ans