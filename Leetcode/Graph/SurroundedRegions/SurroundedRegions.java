package Graph.SurroundedRegions;
// 130. Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

import java.util.Arrays;

// O(m*n) 테두리를 고정하고 내부에서 변경
class Solution {
    char[][] board;
    boolean[][] visited;
    int N;
    int M;

    public void solve(char[][] board) {
        this.M = board.length;
        this.N = board[0].length;

        this.board = board;
        this.visited = new boolean[M][N];

        // 테두리 O 확산 고정
        for (int i = 0; i < M; ++i) {
            if (board[i][0] == 'O' && visited[i][0] != true) {
                isSurrounded(i, 0, false);
            }
            if (board[i][N - 1] == 'O' && visited[i][N - 1] != true) {
                isSurrounded(i, N - 1, false);
            }
        }
        for (int j = 0; j < N; ++j) {
            if (board[0][j] == 'O' && visited[0][j] != true) {
                isSurrounded(0, j, false);
            }
            if (board[M - 1][j] == 'O' && visited[M - 1][j] != true) {
                isSurrounded(M - 1, j, false);
            }
        }

        // 내부 O -> X 변경
        for (int i = 1; i < M - 1; ++i) {
            for (int j = 1; j < N - 1; ++j) {
                if (board[i][j] == 'O' && visited[i][j] != true) {
                    // System.out.println("start" + i + " " + j);
                    isSurrounded(i, j, true);
                }
            }
        }

        return;
    }

    private boolean isSurrounded(int i, int j, boolean isSurround) {
        if (board[i][j] == 'X') {
            return true;
        }

        if (visited[i][j] == true) {
            return isSurround;
        }

        visited[i][j] = true;
        boolean res = true;
        if (i - 1 >= 0) {
            res &= isSurrounded(i - 1, j, isSurround);
        } else {
            res = false;
        }
        if (i + 1 < M) {
            res &= isSurrounded(i + 1, j, isSurround);
        } else {
            res = false;
        }
        if (j - 1 >= 0) {
            res &= isSurrounded(i, j - 1, isSurround);
        } else {
            res = false;
        }
        if (j + 1 < N) {
            res &= isSurrounded(i, j + 1, isSurround);
        } else {
            res = false;
        }

        if (res == true) {
            board[i][j] = 'X';
        }

        return res;
    }
}


public class SurroundedRegions {
    public static void main(String[] args) {
        testSol(new char[][] {{'X', 'X', 'X', 'X'}, {'X', 'O', 'O', 'X'}, {'X', 'X', 'O', 'X'},
                {'X', 'O', 'X', 'X'}},
                new char[][] {{'X', 'X', 'X', 'X'}, {'X', 'X', 'X', 'X'}, {'X', 'X', 'X', 'X'},
                        {'X', 'O', 'X', 'X'}});
        testSol(new char[][] {{'X', 'O', 'X', 'X'}, {'X', 'O', 'O', 'X'}, {'X', 'X', 'O', 'X'},
                {'X', 'O', 'X', 'X'}},
                new char[][] {{'X', 'O', 'X', 'X'}, {'X', 'O', 'O', 'X'}, {'X', 'X', 'O', 'X'},
                        {'X', 'O', 'X', 'X'}});
        testSol(new char[][] {{'X', 'X', 'X', 'X'}, {'X', 'O', 'X', 'X'}, {'X', 'O', 'O', 'X'},
                {'X', 'O', 'X', 'X'}},
                new char[][] {{'X', 'X', 'X', 'X'}, {'X', 'O', 'X', 'X'}, {'X', 'O', 'O', 'X'},
                        {'X', 'O', 'X', 'X'}});
    }

    static String mapToString(char[][] map) {
        String temp = "\n";
        for (int i = 0; i < map.length; ++i) {
            temp += Arrays.toString(map[i]);
            temp += '\n';
        }

        return temp;
    }

    static void testSol(char[][] input, char[][] output) {
        // todo : input, output match
        char[][] out = (char[][]) output;
        Solution sol = new Solution();
        // todo : solution match
        sol.solve(input);
        char[][] res = input;
        if (Arrays.deepEquals(res, out)) {
            System.out.println("O : " + mapToString(res));
        } else {
            System.out.println("x : " + mapToString(res) + "	expect : " + mapToString(out));
        }
    }
}
