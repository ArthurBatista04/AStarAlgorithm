#include "stdio.h"
#include "string.h"
#include <iostream>
#include <unordered_map>
using namespace std;
#include "vector"

int pos00[2] = {0, 0};
int pos01[2] = {0, 1};
int pos02[2] = {0, 2};
int pos03[2] = {0, 3};
int pos10[2] = {1, 0};
int pos11[2] = {1, 1};
int pos12[2] = {1, 2};
int pos13[2] = {1, 3};
int pos20[2] = {2, 0};
int pos21[2] = {2, 1};
int pos22[2] = {2, 2};
int pos23[2] = {2, 3};
int pos30[2] = {3, 0};
int pos31[2] = {3, 1};
int pos32[2] = {3, 2};
int pos33[2] = {3, 3};

class Node
{
public:
    int gValue;
    int heuristic;
    int fValue;
    int numberOfCorrectPieces;
    int numberOfSequeceOfCorrectPieces;
    int manhattamNumber;
    int blankSpace[2];
    int numbers[4][4];
    int numbersInput[16];
    string realInput;
    vector<Node *> childNodes;

    void initTable(int input[])
    {

        for (int i = 0; i < 4; i++)
        {
            for (int j = i * 4; j < 4 * i + 4; j++)
            {
                this->numbers[i][j % 4] = input[j];
            }
        }
    }

    void format()
    {

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cout << numbers[i][j] << " ";
            }
            cout << endl;
        }

        cout << "heu " << heuristic << endl;
        cout << "numberOf " << numberOfCorrectPieces << endl;
        cout << "realinput " << realInput << endl;
        cout << "gvalue " << gValue << endl;
        cout << fValue << endl;
        cout << endl;
    }

    void swap(Node *node, int pos1[2], int pos2[2])
    {

        int aux;
        int x1 = pos1[0];
        int y1 = pos1[1];
        int x2 = pos2[0];
        int y2 = pos2[1];
        memcpy(node->numbers, this->numbers, 16 * sizeof(int));
        aux = this->numbers[x1][y1];
        node->numbers[x1][y1] = this->numbers[x2][y2];
        node->numbers[x2][y2] = aux;
    }

    Node *initChild(int pos1[], int pos2[])
    {
        Node *newNode = new Node();
        swap(newNode, pos1, pos2);
        parseMatrix(newNode);
        findBlankSpace(newNode);
        correctPieces(newNode);
        sequencePieces(newNode);
        manhattam(newNode);
        newNode->gValue = this->gValue + 1;
        newNode->heuristic = h3(newNode);
        newNode->fValue = newNode->gValue + newNode->heuristic;
        return newNode;
    }

    void initNode(int input[])
    {

        initTable(input);
        parseMatrix(this);
        findBlankSpace(this);
        correctPieces(this);
        sequencePieces(this);
        manhattam(this);
        this->gValue = 0;
        this->heuristic = h3(this);
        this->fValue = this->gValue + this->heuristic;
    }

    void parseMatrix(Node *node)
    {
        int pos = 0;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                node->numbersInput[pos] = node->numbers[i][j];
                node->realInput += to_string(node->numbers[i][j]) + " ";
                pos++;
            }
        }
    }

    void findBlankSpace(Node *node)
    {

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (node->numbers[i][j] == 0)
                {
                    node->blankSpace[0] = i;
                    node->blankSpace[1] = j;
                }
            }
        }
    }
    void correctPieces(Node *node)
    {
        int v[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 0}};
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (node->numbers[i][j] == v[i][j])
                {
                    node->numberOfCorrectPieces++;
                }
            }
        }
    }

    void sequencePieces(Node *node)
    {
        int num = node->numbersInput[0];
        for (int i = 1; i < 15; i++)
        {

            if (((num + 1) == node->numbersInput[i + 1]) || (num == 0))
            {
                node->numberOfSequeceOfCorrectPieces++;
            }
            num = node->numbersInput[i + 1];
        }
    }

    void manhattam(Node *node)
    {

        int number, c, d;
        unordered_map<int, vector<int>> rightPositions;
        rightPositions.insert(pair<int, vector<int>>(1, vector<int>{0, 0}));
        rightPositions.insert(pair<int, vector<int>>(2, vector<int>{0, 1}));
        rightPositions.insert(pair<int, vector<int>>(3, vector<int>{0, 2}));
        rightPositions.insert(pair<int, vector<int>>(4, vector<int>{0, 3}));
        rightPositions.insert(pair<int, vector<int>>(5, vector<int>{1, 0}));
        rightPositions.insert(pair<int, vector<int>>(6, vector<int>{1, 1}));
        rightPositions.insert(pair<int, vector<int>>(7, vector<int>{1, 2}));
        rightPositions.insert(pair<int, vector<int>>(8, vector<int>{1, 3}));
        rightPositions.insert(pair<int, vector<int>>(9, vector<int>{2, 0}));
        rightPositions.insert(pair<int, vector<int>>(10, vector<int>{2, 1}));
        rightPositions.insert(pair<int, vector<int>>(11, vector<int>{2, 2}));
        rightPositions.insert(pair<int, vector<int>>(12, vector<int>{2, 3}));
        rightPositions.insert(pair<int, vector<int>>(13, vector<int>{3, 0}));
        rightPositions.insert(pair<int, vector<int>>(14, vector<int>{3, 1}));
        rightPositions.insert(pair<int, vector<int>>(15, vector<int>{3, 2}));
        rightPositions.insert(pair<int, vector<int>>(0, vector<int>{3, 3}));

        for (int a = 0; a < 4; a++)
            for (int b = 0; b < 4; b++)
            {
                number = node->numbers[a][b];
                c = rightPositions.find(number)->second[0];
                d = rightPositions.find(number)->second[1];
                node->manhattamNumber += abs(a - c) + abs(b - d);
            }
    }

    void genSucessors()
    {

        int line = this->blankSpace[0];

        int column = this->blankSpace[1];

        if (line == 0)
        {
            if (column == 0)
            {
                this->childNodes.push_back(initChild(pos00, pos01));
                this->childNodes.push_back(initChild(pos00, pos10));
            }
            else if (column == 1)
            {
                this->childNodes.push_back(initChild(pos01, pos00));
                this->childNodes.push_back(initChild(pos01, pos11));
                this->childNodes.push_back(initChild(pos01, pos02));
            }
            else if (column == 2)
            {
                this->childNodes.push_back(initChild(pos02, pos01));
                this->childNodes.push_back(initChild(pos02, pos12));
                this->childNodes.push_back(initChild(pos02, pos03));
            }
            else if (column == 3)
            {
                this->childNodes.push_back(initChild(pos03, pos02));
                this->childNodes.push_back(initChild(pos03, pos13));
            }
        }
        else if (line == 1)
        {
            if (column == 0)
            {
                this->childNodes.push_back(initChild(pos10, pos00));
                this->childNodes.push_back(initChild(pos10, pos11));
                this->childNodes.push_back(initChild(pos10, pos20));
            }
            else if (column == 1)
            {
                this->childNodes.push_back(initChild(pos11, pos10));
                this->childNodes.push_back(initChild(pos11, pos01));
                this->childNodes.push_back(initChild(pos11, pos12));
                this->childNodes.push_back(initChild(pos11, pos21));
            }
            else if (column == 2)
            {
                this->childNodes.push_back(initChild(pos12, pos11));
                this->childNodes.push_back(initChild(pos12, pos02));
                this->childNodes.push_back(initChild(pos12, pos13));
                this->childNodes.push_back(initChild(pos12, pos22));
            }
            else if (column == 3)
            {
                this->childNodes.push_back(initChild(pos13, pos03));
                this->childNodes.push_back(initChild(pos13, pos12));
                this->childNodes.push_back(initChild(pos13, pos23));
            }
        }
        else if (line == 2)
        {
            if (column == 0)
            {
                this->childNodes.push_back(initChild(pos20, pos10));
                this->childNodes.push_back(initChild(pos20, pos21));
                this->childNodes.push_back(initChild(pos20, pos30));
            }
            else if (column == 1)
            {
                this->childNodes.push_back(initChild(pos21, pos20));
                this->childNodes.push_back(initChild(pos21, pos11));
                this->childNodes.push_back(initChild(pos21, pos22));
                this->childNodes.push_back(initChild(pos21, pos31));
            }
            else if (column == 2)
            {
                this->childNodes.push_back(initChild(pos22, pos21));
                this->childNodes.push_back(initChild(pos22, pos12));
                this->childNodes.push_back(initChild(pos22, pos23));
                this->childNodes.push_back(initChild(pos22, pos32));
            }
            else if (column == 3)
            {
                this->childNodes.push_back(initChild(pos23, pos13));
                this->childNodes.push_back(initChild(pos23, pos22));
                this->childNodes.push_back(initChild(pos23, pos33));
            }
        }
        else if (line == 3)
        {
            if (column == 0)
            {
                this->childNodes.push_back(initChild(pos30, pos20));
                this->childNodes.push_back(initChild(pos30, pos31));
            }
            else if (column == 1)
            {
                this->childNodes.push_back(initChild(pos31, pos30));
                this->childNodes.push_back(initChild(pos31, pos21));
                this->childNodes.push_back(initChild(pos31, pos32));
            }
            else if (column == 2)
            {
                this->childNodes.push_back(initChild(pos32, pos31));
                this->childNodes.push_back(initChild(pos32, pos22));
                this->childNodes.push_back(initChild(pos32, pos33));
            }
            else if (column == 3)
            {
                this->childNodes.push_back(initChild(pos33, pos32));
                this->childNodes.push_back(initChild(pos33, pos23));
            }
        }
    }
    int h1(Node *node)
    {
        return 16 - node->numberOfCorrectPieces;
    }
    int h2(Node *node)
    {
        return 16 - node->numberOfSequeceOfCorrectPieces;
    }

    int h3(Node *node)
    {
        return node->manhattamNumber;
    }

    int h4(Node *node)
    {
        return 0.9 * h1(node) + 0.05 * h2(node) + 0.05 * h3(node);
    }

    int h5(Node *node)
    {
        return maximum(h1(node), h2(node), h3(node));
    }
    int maximum(int a, int b, int c)
    {
        int max = (a < b) ? b : a;
        return ((max < c) ? c : max);
    }
};