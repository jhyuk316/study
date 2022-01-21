package Graph.CourseScheduleII;
// 210. Course Schedule II
// https://leetcode.com/problems/course-schedule-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// O(n) 풀고 나니 Course Schedule 똑같은데 왜 이렇게 어렵게 생각했을까?
class Solution {
    enum Visit {
        before, doing, finish
    };

    private List<List<Integer>> graph;
    private Visit[] visited;
    private List<Integer> result = new ArrayList<>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // list 초기화
        graph = new ArrayList<>();
        visited = new Visit[numCourses];
        for (int i = 0; i < numCourses; ++i) {
            graph.add(new ArrayList<>());
            visited[i] = Visit.before;
        }

        // graph 생성
        for (int[] courses : prerequisites) {
            graph.get(courses[0]).add(courses[1]);
        }
        // System.out.println(graph);

        // 탐색
        for (int i = 0; i < numCourses; ++i) {
            if (hasCycle(i) == true) {
                return new int[] {};
            }
        }

        return result.stream().mapToInt(i -> i).toArray();
    }

    private boolean hasCycle(int node) {
        if (visited[node] == Visit.finish) {
            return false;
        }

        if (graph.get(node).isEmpty()) {
            visited[node] = Visit.finish;
            result.add(node);
            return false;
        }

        if (visited[node] == Visit.doing) {
            return true;
        }
        visited[node] = Visit.doing;
        for (int next : graph.get(node)) {
            if (hasCycle(next) == true) {
                return true;
            }
        }

        visited[node] = Visit.finish;
        result.add(node);
        return false;
    }
}



public class CourseScheduleII {
    public static void main(String[] args) {
        testSol(List.of(2, new int[][] {{1, 0}}), new int[] {0, 1});
        testSol(List.of(4, new int[][] {{1, 0}, {2, 0}, {3, 1}, {3, 2}}), new int[] {0, 2, 1, 3});
        testSol(List.of(1, new int[][] {}), new int[] {0});
        testSol(List.of(2, new int[][] {{1, 0}, {0, 1}}), new int[] {});
        testSol(List.of(4, new int[][] {{2, 1}, {1, 2}, {1, 0}, {3, 1}, {2, 0}, {3, 2}}),
                new int[] {});
        testSol(List.of(7, new int[][] {{3, 3}, {1, 2}}), new int[] {});
        testSol(List.of(4, new int[][] {{2, 1}, {1, 0}, {3, 1}, {2, 0}, {3, 2}}),
                new int[] {0, 1, 2, 3});

    }

    static void testSol(List input, Object output) {
        // todo : input, output match
        int arg1 = (int) input.get(0);
        int[][] arg2 = (int[][]) input.get(1);
        int[] out = (int[]) output;
        Solution sol = new Solution();
        // todo : solution match
        int[] res = sol.findOrder(arg1, arg2);
        if (Arrays.equals(res, out)) {
            System.out.println("O : " + Arrays.toString(res));
        } else {
            System.out
                    .println("x : " + Arrays.toString(res) + "	expect : " + Arrays.toString(out));
        }
    }

}
