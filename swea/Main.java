
import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{

        long[][] answer = new long[91][2];

        int i = 2, j = 1;

        for (int cnt = 1; cnt <= 90; cnt += 1) {
            answer[cnt][0] = i;
            answer[cnt][1] = j;

            int k = i+j;
            j = i;
            i = k;
        }


		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		

		for(int tc = 1; tc <= T; tc += 1)
		{
            int k = sc.nextInt();
            String str = String.format("#%s %s %s", tc, answer[k][0], answer[k][1]);
		
			System.out.println(str);

		}

        sc.close();
	}
}