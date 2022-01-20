package Graph.CourseSchedule;
// 207. Course Schedule
// https://leetcode.com/problems/course-schedule/

import java.util.ArrayList;
import java.util.List;

// O(n) graph를 만들고 dfs로 사이클 체크. memoization으로 단축.
class Solution {
    enum Visit {
        before, doing, finish
    };

    private List<List<Integer>> graph = new ArrayList<>();
    private Visit[] visited;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // List 초기화
        visited = new Visit[numCourses];
        for (int i = 0; i < numCourses; ++i) {
            graph.add(new ArrayList<Integer>());
            visited[i] = Visit.before;
        }

        // Graph 생성
        for (int i = 0; i < prerequisites.length; ++i) {
            int start = prerequisites[i][0];
            int end = prerequisites[i][1];
            graph.get(start).add(end);
        }

        System.out.println(graph);

        // DFS, memoization
        for (int i = 0; i < numCourses; ++i) {
            if (hasCycle(i) == true) {
                return false;
            }
        }

        return true;
    }

    private boolean hasCycle(int node) {
        // finish 표기는 곧, 사이클이 없다는 의미.
        // 사이클이 있으면 이미 true로 끝났음.
        if (visited[node] == Visit.finish) {
            return false;
        } else if (visited[node] == Visit.doing) {
            return true;
        }

        visited[node] = Visit.doing;
        for (int next : graph.get(node)) {
            if (hasCycle(next) == true) {
                return true;
            }
        }

        visited[node] = Visit.finish;
        return false;
    }
}


// O(n) graph를 만들고 dfs로 사이클 체크. memoization으로 단축.
class Solution1 {
    enum Visit {
        before, doing, finish
    };

    private List<List<Integer>> graph = new ArrayList<>();
    private List<Visit> visited = new ArrayList<>();
    private List<Boolean> memo = new ArrayList<>(); // cycle 여부 기록

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // List 초기화
        for (int i = 0; i < numCourses; ++i) {
            graph.add(new ArrayList<Integer>());
            visited.add(Visit.before);
            memo.add(false);
        }

        // Graph 생성
        for (int i = 0; i < prerequisites.length; ++i) {
            Integer s = prerequisites[i][0];
            Integer e = prerequisites[i][1];
            graph.get(s).add(e);
        }

        // System.out.println(graph);

        // DFS, memoization
        for (int i = 0; i < numCourses; ++i) {
            if (hasCycle(i) == true) {
                return false;
            }
        }

        return true;
    }

    private boolean hasCycle(int start) {
        if (visited.get(start) == Visit.finish) {
            return memo.get(start);
        }

        if (visited.get(start) == Visit.doing) {
            visited.set(start, Visit.finish);
            memo.set(start, true);
            return true;
        }

        visited.set(start, Visit.doing);
        boolean result = false;
        for (int next : graph.get(start)) {
            result |= hasCycle(next);
        }

        visited.set(start, Visit.finish);
        memo.set(start, result);
        return result;
    }
}



public class CourseSchedule {
    public static void main(String[] args) {
        testSol(List.of(2, new int[][] {{1, 0}}), true);
        testSol(List.of(2, new int[][] {{1, 0}, {0, 1}}), false);
        testSol(List.of(4, new int[][] {{2, 1}, {1, 2}, {1, 0}, {3, 1}, {2, 0}, {3, 2}}), false);
        testSol(List.of(7, new int[][] {{3, 3}, {1, 2}}), false);
        testSol(List.of(4, new int[][] {{2, 1}, {1, 0}, {3, 1}, {2, 0}, {3, 2}}), true);

    }

    static void testSol(List input, Object output) {
        // todo : input, output match
        int arg1 = (int) input.get(0);
        int[][] arg2 = (int[][]) input.get(1);
        boolean out = (boolean) output;
        Solution sol = new Solution();
        // todo : solution match
        boolean res = sol.canFinish(arg1, arg2);
        if (res == out) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + out);
        }
    }


}
