import java.util.Scanner;

public class Main {
    static int N, M;
    static boolean[] visited;

    static void dfs(int[] sequence, int depth) {
        if (depth == M) {
            for (int num : sequence) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                sequence[depth] = i;
                visited[i] = true;
                dfs(sequence, depth + 1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        visited = new boolean[N + 1];
        dfs(new int[M], 0);
    }

}