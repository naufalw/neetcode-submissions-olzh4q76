#include <vector>
#include <queue>
class Solution {
    bool freshExist(vector<vector<int>>& grid){
        for (int i = 0; i < grid.size(); i++ ){
            for (int j = 0; j < grid[0].size(); j++){
                if (grid[i][j] == 1){
                    return true;
                }
            }
        }

        return false;
    }


public:
    int orangesRotting(vector<vector<int>>& grid) {
        int minutes = 0;
        queue<pair<int, int>> rottens;

        for (int i = 0; i < grid.size(); i++ ){
            for (int j = 0; j < grid[0].size(); j++){
                if (grid[i][j] == 2){
                    rottens.push({i, j});
                }
            }
        }

        while (freshExist(grid)){

            queue<pair<int, int>> new_rottens;
           
            while (!rottens.empty()){
                auto [r, c] = rottens.front();
                rottens.pop();


                if (r > 0 && grid[r-1][c] == 1){
                    grid[r-1][c] = 2;
                    new_rottens.push({r-1, c});
                }

                if (r < grid.size() - 1 && grid[r+1][c] == 1){
                    grid[r+1][c] = 2;
                    new_rottens.push({r+1, c});
                }

                if (c > 0 && grid[r][c-1] == 1){
                    grid[r][c-1] = 2;
                    new_rottens.push({r, c-1});
                }

                if (c < grid[0].size() -1  && grid[r][c+1] == 1){
                    grid[r][c+1] = 2;
                    new_rottens.push({r, c+1});
                }



            }

            if (new_rottens.empty()) return -1;

            rottens.swap(new_rottens);
            minutes++;




        }

        return minutes;
    }
};
