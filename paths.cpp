#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

//const int nNodes {5};

struct Node {

  double x;
  double y;

  };

struct Path {

  //double segment[nNodes];
  //int n;                     // nNodes
  double *segment;           // Length of a segment... actually want array of nodes
                                 // Consider instead a (linked?) list of nodes, a string or arr that gives
                                 // a map for the order, but all point to a single copy of each node
  double length {0};             // Total path length

  };

Path pathFun(Path p) {
//int pathFun() {
  
  cout << "This function will return the best path" << endl;

  //int nNodes {5};     // Not visible to Path struct

  Path bestPath = p;

  return bestPath;
  //return 0;

  }

void path_init(Path p, int n) {

  //double p.segment[n] = {0,1,2};  expects initializer
  p.segment = new double[n];
  //p.segment = {1,2,3};// Can't do this

  }

double dist(Node a, Node b) {

  double dx = a.x - b.x;
  double dy = a.y - b.y;
  double dist = sqrt(dx*dx + dy*dy);
  return dist;

  }

double path_len(Node* a, int n) {

  double sum {0};

  for (int i=0; i<n; i++) {
    sum += dist(a[i], a[i+1]);
    }

  }

int main() {

  Node x0 = {1, 2};
  Node x1 = {2, 3};

  cout << x0.x << endl;

  int nNodes = 3;

  double X[] = {1, 4, 7};
  double Y[] = {3, 6, 5};
  Node nodes[nNodes];
  
  for (int i=0; i < nNodes; i++) {
    
    nodes[i] = {X[i], Y[i]};

    }

  Path path0;
  path_init(path0, nNodes);
  //path0.segment = new double[nNodes];

  //Node nodes[] = {x0, x1};

  pathFun(path0);

  //cout << pathFun(path0) << endl; // can't print Path object
  cout << path0.length << endl;
  cout << "All good" << endl;
  cout << path0.segment[4] << endl;
  for (auto x : X)
    cout << x << ' ';
  cout << endl;
  for (int i=0; i<7; i++) {
  cout << next_permutation(X, X+3) << endl;
  for (auto x : X)
    cout << x << ' ';
  cout << endl;}
  cout << dist(x0,x1) << endl;
  cout << dist(nodes[0], nodes[1]) << endl;
  cout << path_len(nodes, nNodes) << endl;

  }






