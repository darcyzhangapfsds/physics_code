#include <iostream>
#include <vector>
using namespace std;

int main() {
    int rows;int cols;int nums;int ycount;int moves;int rotation;
    rotation = rows+cols;
    scanf("%d",&rows);scanf("%d",&cols);scanf("%d",&moves);
    int global[rows][cols] = {};
    for(int a=0;a<rows;a++) {
        for (int b=0;b<cols;b++) {
            global[a][b] = a+b;
        }
    }
    vector<int> localvars;
    for(int=0;a<rotation) {
        localvars.push_back(i+1);
        cout << localvars.size();
    }
}

void returnlocal() {
    for(int i=0;i<cols;i++) {
        string choice;int local;
        scanf("%s",&choice);scanf("%d",&local);
        if(choice=="R") {
            for(int c=0;c<rows;c++) {
                if(global[local][c] == "B") {
                    global[local][c] == "G";
                }
                else {
                    global[local][c] == "B";
                }
            }
        }
        else {
            for(int d=0;d<cols;d++) {
                if(global[d][local] == "B") {
                    global[d][local] == "G";
                }
                else {
                    global[d][local] == "B";
                }
            }
        }
    }
    for(int m=0;m<rows;m++) {
        for(int n=0;n<rows;n++) {
            if(global[n][m] == "G") {
                ycount++;
            }
            else {
                ycount=ycount;
            }
        }
    }
    for(int k=0;k<ycount;k++) {
        for(int u=0;u<ycount;u++) {
            cout << global[k][u];
        }
    }
    return 0;
}
