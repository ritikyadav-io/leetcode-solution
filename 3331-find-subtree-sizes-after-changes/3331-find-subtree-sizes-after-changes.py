from typing import List


class Solution:

  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(parent)
    orig_adj = [[] for _ in range(n)]
    for i in range(1, n):
      orig_adj[parent[i]].append(i)

    new_parent = parent[:]
    last_char = [-1] * 26

    def dfs_rewire(u: int) -> None:
      idx = ord(s[u]) - ord("a")
      if last_char[idx] != -1:
        new_parent[u] = last_char[idx]

      prev = last_char[idx]
      last_char[idx] = u

      for v in orig_adj[u]:
        dfs_rewire(v)

      last_char[idx] = prev

    dfs_rewire(0)

    new_adj = [[] for _ in range(n)]
    for i in range(1, n):
      new_adj[new_parent[i]].append(i)

    ans = [1] * n

    def dfs_size(u: int) -> int:
      size = 1
      for v in new_adj[u]:
        size += dfs_size(v)
      ans[u] = size
      return size

    dfs_size(0)
    return ans
