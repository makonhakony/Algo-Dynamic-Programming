# Algo-Dynamic-Programming
This is created to save knowledge about Dynamic Programming

## Most obvious use case
For the problem we need to find the Min/Max or the sequence, that the later decision can change the outcome

The most common problem:
- [fibonanci](https://leetcode.com/problems/fibonacci-number/description/) [Solution✔️]
- [House robber](https://leetcode.com/problems/house-robber/description/) [Solution✔️]
- [Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/) [Solution✔️]

## Memoization
(aka Top-down or Recursive)
``` Python 3
def minCost(colors: str, neededTime: List[int], i: int) -> int:
    if i == len(colors) - 1:
        return 0
    if colors[i] == colors[i + 1]:
        time = min(neededTime[i], neededTime[i + 1])
        neededTime[i + 1] = max(neededTime[i], neededTime[i + 1])
        return time + minCost(colors, neededTime, i + 1)
    else:
        return minCost(colors, neededTime, i + 1)

```


## Tabulation
(aka Bottom-up or Iterative)
``` Python 3
def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        n = len(colors)
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                time += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return time
```
