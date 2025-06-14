// Last updated: 6/14/2025, 10:34:28 PM
class Solution {
public:
    int reverse(int x) {
          long  m=x;
          m=abs(m);
        long t=0;
        long long rev =0;

        while(m>0)
        {
            t=m%10;
            m=m/10;
            rev= (rev*10)+t;
            if(rev>INT_MAX)
            {return 0;
            }
        }
        if(x>0)
        return rev;
        else 
        return  -rev;
    }
};