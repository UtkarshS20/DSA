// Display longest name
// https://www.geeksforgeeks.org/problems/display-longest-name0853/1?page=1&category=Strings&difficulty=School,Basic,Easy&sortBy=difficulty
class Solution{
    public:
    string longest(string names[], int n)
    {
        int max_length = INT_MIN;
        string ans = "";
        for (int i = 0; i<n; i++)
        {
            int len = names[i].length();
            max_length = max(max_length,len);
        }
        for (int i = 0; i<n; i++)
        {
            if (names[i].length()==max_length)
            return names[i];
        }
    }
};