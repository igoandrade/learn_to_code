public class Teste {
    public static int[][] Matrix(int[][] mat, int length, int col, int row) {
        int[][] m = new int[length][length];
        int n = length / 2;
        for (int i = 0; i < length; i++) {
            int c = col - n + i;
            if (c < 0) c = c + mat[0].length;
            if (c >= mat[0].length) c = c % mat[0].length;
            for (int j = 0; j < length; j++) {
                int r = row - n + j;
                if (r < 0) r = r + mat.length;
                if (r >= mat.length) r = r % mat.length;
                m[j][i] = mat[r][c];  
            }
        } 
        return m;       
    }
    public static int[][] newMatrix(int[][] mat) {
        int[][] base = {
            {1, 2, 0},
            {0, 5, -4},
            {0, -3, 0}
        };
        int length = base.length;
        int[][] m = new int[mat.length][mat[0].length];
        for (int col = 0; col < mat[0].length; col++) {
            for (int row = 0; row < mat.length; row++) {
                int newVal = 0;
                int[][] matrix = Matrix(mat, length, col, row);
                for (int i = 0; i < length; i++) {
                    for (int j = 0; j < length; j++) {
                        newVal += base[i][j] * matrix[i][j];
                    }
                }
                if (newVal < 0) newVal = 0;
                if (newVal > 255) newVal = 255;
                m[row][col] = newVal;
            }
        }
        return m;

    }
    public static void imprimeMatrix(int[][] mat) {
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                StdOut.print(mat[i][j] + " ");
            }
            StdOut.println();
        }
    }
    public static void main(String[] args) {
        int length = Integer.parseInt(args[0]);
        int row = Integer.parseInt(args[1]);
        int col = Integer.parseInt(args[2]); 
        int[][] mat = {
            {255,  45,   0,   0,   0,   0},
            { 23,  66,  10,  50,  40,  78},
            { 45,  22, 120,  60,  70,  67},
            { 79,  34, 100,  30,  20,  56},
            { 61,  45,  33,  66,  43, 160},
        };
        imprimeMatrix(mat);
        StdOut.println();
        int[][] m = Matrix(mat, length, col, row);
        imprimeMatrix(m);
        StdOut.println();
        imprimeMatrix(newMatrix(mat));
    }
}
