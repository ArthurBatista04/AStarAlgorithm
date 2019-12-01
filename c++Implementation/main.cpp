#include "stdio.h"
#include <iostream>
#include "./node.cpp"
#include <string>
#include <iterator>
#include <sstream>
#include <iterator>
#include <unordered_map>
#include <queue>
using namespace std;

struct compare
{
    bool operator()(pair<int, Node *> pair1, pair<int, Node *> pair2)
    {
        return pair1.first > pair2.first;
    }
};

int *parseInput()
{
    int *input = (int *)malloc(16 * sizeof(int));
    for (int i = 0; i < 16; i++)
    {
        cin >> input[i];
    }
    return input;
}

bool contains(unordered_map<string, Node *> &dict, string &key)
{
    unordered_map<string, Node *>::iterator it = dict.find(key);
    return (it != dict.end());
}

int aStarAlgorithm(Node *S)
{
    unordered_map<string, Node *> A;
    unordered_map<string, Node *> F;

    priority_queue<pair<int, Node *>, vector<pair<int, Node *>>, compare> queue;
    string tableKey = S->realInput;

    A.insert(make_pair(tableKey, S));
    queue.push(make_pair(S->fValue, S));

    pair<int, Node *> v = pair<int, Node *>(S->fValue, S);
    while (true)
    {
        pair<int, Node *> v = queue.top();
        string tableKey = v.second->realInput;

        if (v.second->numberOfCorrectPieces == 16)
        {
            return v.second->gValue;
        }
        F.insert(make_pair(tableKey, v.second));
        A.erase(tableKey);
        queue.pop();
        v.second->genSucessors();

        for (Node *child : v.second->childNodes)
        {
            string childKey = child->realInput;
            if (contains(A, childKey) && child->gValue < A.find(childKey)->second->gValue)
            {
                A.erase(childKey);
            }
            if (!contains(A, childKey) && !contains(F, childKey))
            {
                A.insert(make_pair(childKey, child));
                queue.push(make_pair(child->fValue, child));
            }
        }
    }
    return v.second->gValue;
}

int main(int argc, char const *argv[])
{

    Node *node = new Node();
    int *input = parseInput();
    node->initNode(input);
    int result = aStarAlgorithm(node);
    cout << result;
}
