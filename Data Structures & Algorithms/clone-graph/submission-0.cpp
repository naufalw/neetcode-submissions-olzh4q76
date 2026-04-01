/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

#include <unordered_map>
#include <queue>
#include <vector>

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node){
            return nullptr;
        }

        std::unordered_map<Node*, Node*> visited;
        std:queue<Node*> q;

        visited[node] = new Node(node->val);

        q.push(node);

        while (!q.empty()){
            Node* curr = q.front();
            q.pop();

            for (Node* neighbor : curr -> neighbors){
                if (visited.find(neighbor) == visited.end()){
                    visited[neighbor] = new Node(neighbor -> val);
                    q.push(neighbor);
                }

                visited[curr]->neighbors.push_back(visited[neighbor]);
            }
        }

        return visited[node];

    }
};
