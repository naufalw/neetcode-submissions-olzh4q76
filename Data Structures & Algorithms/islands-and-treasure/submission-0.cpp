#include <set>
#include <queue>

class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        if(grid.empty()){
            return;
        }
        int m = grid.size();
        int n = grid[0].size();
        int INF = 2147483647;
        std::queue<pair<int, int>> q;

        for (int r = 0; r < m; r++){
            for (int c = 0; c < n; c++){
                if (grid[r][c] == 0){
                    q.push({r, c});
                }
            }
        }

        while (!q.empty()){
            pair<int, int> cur = q.front();
            q.pop();
            int r = cur.first;
            int c = cur.second;
            int curDist = grid[r][c];
        

            if (r > 0 && grid[r-1][c] == INF){
                grid[r-1][c] = curDist + 1;
                q.push({r-1, c});
            }

            if (r < m - 1 && grid[r+1][c] == INF){
                grid[r+1][c] = curDist + 1;
                q.push({r+1, c});
            }

            if (c > 0 && grid[r][c-1] == INF){
                grid[r][c-1] = curDist + 1;
                q.push({r, c-1});
            }

            if (c < n - 1 && grid[r][c+1] == INF){
                grid[r][c+1] = curDist + 1;
                q.push({r, c+1});
            }
        }
        
    }
};
