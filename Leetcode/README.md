# LeetCode 풀어보기

- [알고리즘 전략](#알고리즘-전략)
  - [완전 탐색(Brute force)](#완전-탐색brute-force)
  - [정렬](#정렬)
  - [이분 탐색(Binary Search)](#이분-탐색binary-search)
  - [해싱](#해싱)
  - [탐욕법(Greedy)](#탐욕법greedy)
  - [동적 계획법(Dynamic Programing)](#동적-계획법dynamic-programing)
  - [분할 정복(Divide and Conquer)](#분할-정복divide-and-conquer)
  - [스택/큐](#스택큐)
  - [힙](#힙)
  - [깊이/너비 우선 탐색(DFS/BFS)](#깊이너비-우선-탐색dfsbfs)
  - [그래프](#그래프)
- [추천 문제 75선](#추천-문제-75선)
  - [Array](#array)
  - [Binary](#binary)
  - [Dynamic Programming](#dynamic-programming)
  - [Graph](#graph)
  - [Interval](#interval)
  - [Linked List](#linked-list)
  - [Matrix](#matrix)
  - [String](#string)
  - [Tree](#tree)
  - [Heap](#heap)
- [개인적으로 풀어 본 것](#개인적으로-풀어-본-것)
  - [Array](#array-1)
  - [Binary](#binary-1)
  - [Dynamic Programming](#dynamic-programming-1)
  - [Graph](#graph-1)
  - [Interval](#interval-1)
  - [Linked List](#linked-list-1)
  - [Matrix](#matrix-1)
  - [String](#string-1)
  - [Tree](#tree-1)
  - [Heap](#heap-1)
  - [Math](#math)
  - [backtracking](#backtracking)

## 알고리즘 전략

- 알고리즘이란?

  인간이 문제 해결을 위해서 사용하는 모호한 방법과 사고를 논리적으로 절차에 따라 기술하는 것.

  문제를 해결하기 위한 절차나 방법.

### 완전 탐색(Brute force)

- 모든 경우의 수를 탐색
- 수행 속도는 느리지만 해답을 찾기는 쉬움.
- 다른 알고리즘의 해답으로 사용

### 정렬

- 정렬을 이용하여 해결

### 이분 탐색(Binary Search)

- 정렬된 데이터를 빠르게 탐색

### 해싱

- 키를 이용해 빠른 탐색

### 탐욕법(Greedy)

- 최적해를 구하는 데 사용되는 근시안적인 방법, 직관.

- 부분 최적해가 전체의 최적해가 됨.
- 지금 이 순간의 최선의 선택이 최종적으로 최선의 답.

- 그리디 알고리즘이 적용 가능한 곳

  - 탐욕 선택 속성(greedy choice property)
    - 이전 선택과 무관하게 현재의 선택이 매 순간 최적해.
  - 최적 부분 구조(optimal substructure)
    - 부분 최적해의 집합이 전체 최적해.

- 문제를 작은 문제로 분할하여 부분해 찾음.

- 장점 : 직관적인 해결이 가능?
- 단점 : 일반적으로 부분 최적해가 전체 최적해가 되지 않으므로 현실적이지 않음. 그것이 가능한 문제에서만 사용해야 함.

### 동적 계획법(Dynamic Programing)

- 비효율적인 게산을 줄여 효율적으로 해를 찾음.
- 메모이제이션 - 반복적인 계산의 결과를 저장해 둠으로써 연산을 줄임.

### 분할 정복(Divide and Conquer)

- 큰 문제를 분할하여 작은 문제로 만들어 해결 후 결과를 합치는 것.
- 분할 - 정복 - 조합의 과정을 거침.

### 스택/큐

- LIFO, FIFO 문제를 해결하기 위한 자료구조.

### 힙

- 특정한 규칙을 가진 트리 구조로 빠른 삽입, 제거, 정렬 가능.

### 깊이/너비 우선 탐색(DFS/BFS)

- 그래프를 올바르게 탐색하기 위한 방법
- Backtracking

- DFS : 그래프를 깊게 들어가서 끝에서부터 처리. Bottom-up?
- BFS : 그래프 위에서부터 모든 노드들을 처리해가면서 내려감. Top-Down?

- 구현
  - DFS : 문제를 'Stack'에 넣고 빼면서 처리
  - BFS : 문제를 'Queue'에 넣고 빼면서 처리

### 그래프

- 노드와 에지로 이루어진 자료구조.

## 추천 문제 75선

아래의 추천 문제를 모두 풀어 보는 것을 목표로 함.

New Year Gift - Curated List of Top 75 LeetCode Questions to Save Your Time

출처 - <https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU>

### Array

- [x] O(n) 1. Two Sum - <https://leetcode.com/problems/two-sum/>
- [x] O(n) 121. Best Time to Buy and Sell Stock - <https://leetcode.com/problems/best-time-to-buy-and-sell-stock/>
- [x] O(n) 217. Contains Duplicate - <https://leetcode.com/problems/contains-duplicate/>
- [x] O(n) 238. Product of Array Except Self - <https://leetcode.com/problems/product-of-array-except-self/>
- [x] O(n) 53. Maximum Subarray - <https://leetcode.com/problems/maximum-subarray/>
- [x] O(n) 152. Maximum Product Subarray - <https://leetcode.com/problems/maximum-product-subarray/>
- [x] O(logn) 153. Find Minimum in Rotated Sorted Array - <https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/>
- [x] O(logn) 33. Search in Rotated Sorted Array - <https://leetcode.com/problems/search-in-rotated-sorted-array/>
- [x] O(n^2) 15. 3Sum - <https://leetcode.com/problems/3sum/>
- [x] O(n) 11. Container With Most Water - <https://leetcode.com/problems/container-with-most-water/>

### Binary

- [x] O(1?) 371. Sum of Two Integers - <https://leetcode.com/problems/sum-of-two-integers/>
- [x] O(n) 191. Number of 1 Bits - <https://leetcode.com/problems/number-of-1-bits/>
- [x] O(n) 338. Counting Bits - <https://leetcode.com/problems/counting-bits/>
- [x] O(n) 268. Missing Number - <https://leetcode.com/problems/missing-number/>
- [x] O(n) 190. Reverse Bits - <https://leetcode.com/problems/reverse-bits/>

### Dynamic Programming

- [x] O(n) 70. Climbing Stairs - <https://leetcode.com/problems/climbing-stairs/>
- [x] O(m\*n) 322. Coin Change - <https://leetcode.com/problems/coin-change/>
- [x] O(n\*logn) 300. Longest Increasing Subsequence - <https://leetcode.com/problems/longest-increasing-subsequence/>
- [x] O(m\*n) 1143. Longest Common Subsequence - <https://leetcode.com/problems/longest-common-subsequence/>
- [x] O(m\*n) 139. Word Break Problem - <https://leetcode.com/problems/word-break/>
- [x] O(m\*n) 377. Combination Sum - <https://leetcode.com/problems/combination-sum-iv/>
- [x] O(n) 198. House Robber - <https://leetcode.com/problems/house-robber/>
- [x] O(n) 213. House Robber II - <https://leetcode.com/problems/house-robber-ii/>
- [x] O(n) 91. Decode Ways - <https://leetcode.com/problems/decode-ways/>
- [ ] Unique Paths - <https://leetcode.com/problems/unique-paths/>
- [ ] Jump Game - <https://leetcode.com/problems/jump-game/>

### Graph

- [x] O(n) 133. Clone Graph - <https://leetcode.com/problems/clone-graph/>
- [x] O(n) 207. Course Schedule - <https://leetcode.com/problems/course-schedule/>
- [ ] Pacific Atlantic Water Flow - <https://leetcode.com/problems/pacific-atlantic-water-flow/>
- [ ] Number of Islands - <https://leetcode.com/problems/number-of-islands/>
- [ ] Longest Consecutive Sequence - <https://leetcode.com/problems/longest-consecutive-sequence/>
- [ ] Alien Dictionary (Leetcode Premium) - <https://leetcode.com/problems/alien-dictionary/>
- [ ] Graph Valid Tree (Leetcode Premium) - <https://leetcode.com/problems/graph-valid-tree/>
- [ ] Number of Connected Components in an Undirected Graph (Leetcode Premium) - <https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/>

### Interval

- [x] O(n) 57. Insert Interval - <https://leetcode.com/problems/insert-interval/>
- [ ] Merge Intervals - <https://leetcode.com/problems/merge-intervals/>
- [ ] Non-overlapping Intervals - <https://leetcode.com/problems/non-overlapping-intervals/>
- [ ] Meeting Rooms (Leetcode Premium) - <https://leetcode.com/problems/meeting-rooms/>
- [ ] Meeting Rooms II (Leetcode Premium) - <https://leetcode.com/problems/meeting-rooms-ii/>

### Linked List

- [x] O(n) 206. Reverse a Linked List - <https://leetcode.com/problems/reverse-linked-list/>
- [x] O(n^2?) 141. Detect Cycle in a Linked List - <https://leetcode.com/problems/linked-list-cycle/>
- [ ] Merge Two Sorted Lists - <https://leetcode.com/problems/merge-two-sorted-lists/>
- [ ] Merge K Sorted Lists - <https://leetcode.com/problems/merge-k-sorted-lists/>
- [ ] Remove Nth Node From End Of List - <https://leetcode.com/problems/remove-nth-node-from-end-of-list/>
- [ ] Reorder List - <https://leetcode.com/problems/reorder-list/>

### Matrix

- [x] space: O(1) 73. Set Matrix Zeroes - <https://leetcode.com/problems/set-matrix-zeroes/>
- [x] O(m\*n) 54. Spiral Matrix - <https://leetcode.com/problems/spiral-matrix/>
- [x] O(n^2) 48. Rotate Image - <https://leetcode.com/problems/rotate-image/>
- [ ] Word Search - <https://leetcode.com/problems/word-search/>

### String

- [x] O(n) 3. Longest Substring Without Repeating Characters - <https://leetcode.com/problems/longest-substring-without-repeating-characters/>
- [x] O(n) 424. Longest Repeating Character Replacement - <https://leetcode.com/problems/longest-repeating-character-replacement/>
- [x] O(??) 76. Minimum Window Substring - <https://leetcode.com/problems/minimum-window-substring/>
- [x] O(m+n) 242. Valid Anagram - <https://leetcode.com/problems/valid-anagram/>
- [x] O(m\*n\*logn) 49. Group Anagrams - <https://leetcode.com/problems/group-anagrams/>
- [x] O(n) 20. Valid Parentheses - <https://leetcode.com/problems/valid-parentheses/>
- [x] O(n) 125. Valid Palindrome - <https://leetcode.com/problems/valid-palindrome/>
- [x] O(n^2) 5. Longest Palindromic Substring - <https://leetcode.com/problems/longest-palindromic-substring/>
- [ ] Palindromic Substrings - <https://leetcode.com/problems/palindromic-substrings/>
- [ ] Encode and Decode Strings (Leetcode Premium) - <https://leetcode.com/problems/encode-and-decode-strings/>

### Tree

- [x] O(n) 104. Maximum Depth of Binary Tree - <https://leetcode.com/problems/maximum-depth-of-binary-tree/>
- [x] O(n) 100. Same Tree - <https://leetcode.com/problems/same-tree/>
- [ ] Invert/Flip Binary Tree - <https://leetcode.com/problems/invert-binary-tree/>
- [ ] Binary Tree Maximum Path Sum - <https://leetcode.com/problems/binary-tree-maximum-path-sum/>
- [ ] Binary Tree Level Order Traversal - <https://leetcode.com/problems/binary-tree-level-order-traversal/>
- [ ] Serialize and Deserialize Binary Tree - <https://leetcode.com/problems/serialize-and-deserialize-binary-tree/>
- [ ] Subtree of Another Tree - <https://leetcode.com/problems/subtree-of-another-tree/>
- [ ] Construct Binary Tree from Preorder and Inorder Traversal - <https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/>
- [ ] Validate Binary Search Tree - <https://leetcode.com/problems/validate-binary-search-tree/>
- [ ] Kth Smallest Element in a BST - <https://leetcode.com/problems/kth-smallest-element-in-a-bst/>
- [ ] Lowest Common Ancestor of BST - <https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/>
- [ ] Implement Trie (Prefix Tree) - <https://leetcode.com/problems/implement-trie-prefix-tree/>
- [ ] Add and Search Word - <https://leetcode.com/problems/add-and-search-word-data-structure-design/>
- [ ] Word Search II - <https://leetcode.com/problems/word-search-ii/>

### Heap

- [ ] Merge K Sorted Lists - <https://leetcode.com/problems/merge-k-sorted-lists/>
- [ ] Top K Frequent Elements - <https://leetcode.com/problems/top-k-frequent-elements/>
- [ ] Find Median from Data Stream - <https://leetcode.com/problems/find-median-from-data-stream/>

---

## 개인적으로 풀어 본 것

### Array

- [x] O(n) 반복 O, 재귀 X 344. Reverse String <https://leetcode.com/problems/reverse-string/>
- [x] O(n) 977. Squares of a Sorted Array <https://leetcode.com/problems/squares-of-a-sorted-array/>
- [x] O(n) 134. <https://leetcode.com/problems/gas-station/>

### Binary

### Dynamic Programming

### Graph

### Interval

### Linked List

- [x] O(n) 2. Add Two Numbers <https://leetcode.com/problems/add-two-numbers/>

### Matrix

### String

- [x] O(n\*logn) 179. Largest Number <https://leetcode.com/problems/largest-number/>

### Tree

### Heap

### Math

### backtracking

- [x] 52. N-Queens II <https://leetcode.com/problems/n-queens-ii/>
