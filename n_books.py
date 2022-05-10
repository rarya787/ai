'''
Problem Statement:
Given an array of ratings for n books. Find the minimum cost to buy all books with below conditions:
1. Cost of every book would be at-least 1 dollar.
2. A book has higher cost than an adjacent (left or right) if rating is more than the adjacent.

Aim:
To find the minimum cost to buy all books.

Procedure:
1. Make two arrays left2right and right2left and fill 1 in both of them.
2. Traverse left to right and fill left2right array and update it by seeing previous rating of given
array. Do not care about next rating of given array.
3. Traverse right to left and fill right2left array and update it by seeing next rating of given
array. Do not care about previous rating of given array.
4. Find maximum value of ith position in both array (left2right and right2left) and add it to
result
'''

def minCost(ratings, n):
  res = 0
  left2right = [1 for i in range(n)]
  right2left = [1 for i in range(n)]
  for i in range(1, n):
    if (ratings[i] &gt; ratings[i - 1]):
      left2right[i] = left2right[i - 1] + 1
  i = n - 2
  while(i &gt;= 0):
    if (ratings[i] &gt; ratings[i + 1]):
      right2left[i] = right2left[i + 1] + 1
    i -= 1
  for i in range(n):
    res += max(left2right[i], right2left[i])
  return res
  
print(&quot;Ratings of n books: &quot;)
ratings = list(map(int, input().split(&#39; &#39;)))
n = len(ratings)
print(&quot;minimum cost: &quot;, minCost(ratings, n))
