import java.nio.file.*;
import static java.util.Arrays.stream;
import java.util.*;
import java.lang.*;
import java.text.*;

public class euler18 {
 
    public static void main(String[] args) throws Exception {
        long startTime = System.nanoTime();

        int[][] data = Files.lines(Paths.get("euler18.txt"))
                .map(s -> stream(s.trim().split("\\s+"))
                        .mapToInt(Integer::parseInt)
                        .toArray())
                .toArray(int[][]::new);
 
        for (int r = data.length - 1; r > 0; r--)
            for (int c = 0; c < data[r].length - 1; c++)
                data[r - 1][c] += Math.max(data[r][c], data[r][c + 1]);
 
        System.out.println(data[0][0]);
        long endTime = System.nanoTime();

        long timeElapsed = endTime - startTime;

        System.out.println("Execution time in nanoseconds: " + timeElapsed);
        System.out.println("Execution time in milliseconds: " + timeElapsed / 1000000);
    }
}

/*
1074
Execution time in nanoseconds: 21708567
Execution time in milliseconds: 21
*/