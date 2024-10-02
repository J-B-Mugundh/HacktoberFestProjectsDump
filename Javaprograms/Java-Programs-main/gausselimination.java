public class gausselimination {
    private static final double EPSILON = 1e-10;

    // The following is a program for Gaussian elimination using the partial pivoting method
    public static double[] solution(double[][] A, double[] b) {
        // Inputting the coefficient matrix and the column vector of solutions
        int n = b.length;

        for (int p = 0; p < n - 1; p++) {
            // Finding the pivot row and swapping
            int max = p;
            for (int i = p + 1; i < n; i++) {
                if (Math.abs(A[i][p]) > Math.abs(A[max][p])) {
                    max = i;
                }
            }

            // Swap rows in matrix A
            double[] temp = A[p];
            A[p] = A[max];
            A[max] = temp;

            // Swap corresponding values in vector b
            double t = b[p];
            b[p] = b[max];
            b[max] = t;

            // If the matrix is singular or near-singular
            if (Math.abs(A[p][p]) <= EPSILON) {
                throw new ArithmeticException("Matrix is partially or completely singular");
            }

            // Perform row elimination
            for (int i = p + 1; i < n; i++) {
                double alpha = A[i][p] / A[p][p];
                b[i] -= alpha * b[p];
                for (int j = p; j < n; j++) {
                    A[i][j] -= alpha * A[p][j];
                }
            }
        }

        // Code for back substitution
        double[] x = new double[n];
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0.0;
            for (int j = i + 1; j < n; j++) {
                sum += A[i][j] * x[j];
            }
            x[i] = (b[i] - sum) / A[i][i];
        }

        return x;
    }

    // Sample input for the method
    public static void main(String[] args) {
        int n = 3;  // Corrected matrix size
        double[][] A = { {0, 1, 1}, {2, 4, -2}, {0,3,15 }};
        double[] b = {4,2,36};

        // Printing results
        double[] x = solution(A, b);
        for (int i = 0; i < n; i++) {
            System.out.println(x[i]);
        }
    }
}
