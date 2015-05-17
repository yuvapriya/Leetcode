using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
  public class Solution {
      static void Main(string[] args)
        {
            Solution s = new Solution();
             int[,] m = {{ 1, 2, 3 }, { 4, 5, 6 }, {7, 8, 9 }};
          int[,] n = {{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}};
          int[,] p = {{0}};
             Console.WriteLine(s.SpiralOrder(m));
             //Console.WriteLine(s.SpiralOrder(n));
             //Console.WriteLine(s.GenerateMatrix(3));
             //s.SetZeroes(p);
          s.Rotate(m);
             Console.ReadLine();
        }
    public IList<int> SpiralOrder(int[,] matrix) {
        IList<int> result = new List<int>();
        int sr = 0, sc = 0, er = matrix.GetLength(0) - 1, ec = matrix.GetLength(1) - 1;
        while(sr<=er && sc <=ec) { 
            //print first row
            for (int f = sc; f <= ec; f++)
                result.Add(matrix[sr, f]);
            sr++;
            //print last col
            for (int f = sr; f <= er; f++)
                result.Add(matrix[f, ec]);
            ec--;
            //print last row right to left
            for (int f = ec; f >= sc && sr <= er; f--)
                result.Add(matrix[er, f]);
            er--;
            //print first col bottom up
            for (int f = er; f >= sr && sc <= ec; f--)
                result.Add(matrix[f, sc]);
            sc++;
        }
        
        return result;
    }
    public int[,] GenerateMatrix(int n)
    {
        int[,] matrix = new int[n, n];
        int sr = 0, sc = 0, er = matrix.GetLength(0) - 1, ec = matrix.GetLength(1) - 1;
        int count = 1;
        while (sr <= er && sc <= ec)
        {
            //print first row
            for (int f = sc; f <= ec; f++)
                matrix[sr, f] = count++;
            sr++;
            //print last col
            for (int f = sr; f <= er; f++)
                matrix[f, ec] = count++;
            ec--;
            //print last row right to left
            for (int f = ec; f >= sc && sr <= er; f--)
                matrix[er, f] = count++;
            er--;
            //print first col bottom up
            for (int f = er; f >= sr && sc <= ec; f--)
                matrix[f, sc] = count++;
            sc++;
        }
        return matrix;
    }
    public void SetZeroes(int[,] matrix)
    {
        int rows = matrix.GetLength(0);
        int cols = matrix.GetLength(1);
        int[] r = new int[rows];
        int[] c = new int[cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i, j] == 0) {
                    r[i] = 1;
                    c[j] = 1;
                }
            }
        }
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (r[i] == 1 || c[j] == 1)
                {
                    matrix[i, j] = 0;
                }
            }
        }

    }
    public bool SearchMatrix(int[,] matrix, int target)
    {
        int rows = matrix.GetLength(0);
        int cols = matrix.GetLength(1);
        int sc = 0;
        // start from last row
        for (int i = rows - 1; i >=0; i--)
        {
            for (int j = sc; j < cols; j++)
            {
                if (matrix[i, j] == target)
                {
                    return true;
                }
                //ignore row
                else if (matrix[i, j] > target)
                {
                    break;
                }                
            }
        }
        return false;
    }
    public void Rotate(int[,] matrix)
    {
        int n = matrix.GetLength(0);
        for (int first = 0; first < n / 2; first++) {
            int last = n - first - 1;
            for (int j = first; j < last; j++) {
                int offset = j-first;
                int top = matrix[first, j]; //save top
                matrix[first, j] = matrix[last-offset, first]; //left to top

                matrix[last-offset, first] = matrix[last, last-offset];     //bottom to left
                matrix[last, last-offset] = matrix[j, last]; //right to bottom
                matrix[j, last] = top;//top to right
            }
        }
    }

        
}