#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

struct Node {

  int x;                        // rand generates int, avoid narrowing conversion warning
  int y;
  int id;                       // identify the node for permutation purposes
  string coords() {
    string xstr = to_string(x);
    string ystr = to_string(y);
    return '(' + xstr + ", " + ystr + ") ";
    }

  };

//struct Path {
//
//  double *segment;           // Length of a segment... actually want array of nodes
//                                 // Consider instead a (linked?) list of nodes, a string or arr that gives
//                                 // a map for the order, but all point to a single copy of each node
//  double length {0};             // Total path length
//
//  };
//
//void path_init(Path& p, int n) {
//
//  p.segment = new double[n];
//
//  }

double dist(Node a, Node b) {

  double dx = a.x - b.x;
  double dy = a.y - b.y;
  double dist = sqrt(dx*dx + dy*dy);
  return dist;

  }

double path_len(Node* a, int n) {

  double sum {0};

  for (int i=0; i<n-1; i++) {
    sum += dist(a[i], a[i+1]);
    }

  return sum;

  }

int main() {
  
  srand(time(NULL));          // Careful of repeat calls?

  int nNodes = 11;

  int indx[nNodes];
  Node nodes[nNodes];
  Node original[nNodes];                // Holds original arrangement of nodes for permuting
  Node best[nNodes];                    // Store best path

  for (int i=0; i<nNodes; i++) {
    original[i] = {rand() % 100, rand() % 100, i};      // narrowing conversion
    //nodes[i] = original[i];
    indx[i] = i;
    }

  //double best_len {path_len(original, nNodes)}; // Problem if first is shortest (never assigns best[])
  double best_len {1e300};
  double temp_len;

  do {
    //for (int elem : indx) {
    //  cout << elem << ' ';
    //  }
    //cout << endl;
    //for (int elem : indx) {        // equivalent option?
    for (int j=0; j<nNodes; j++) {
      nodes[j] = original[indx[j]];
      //cout << nodes[j].coords();
      }
    temp_len = path_len(nodes, nNodes);
    //cout << temp_len << endl;
    if (temp_len < best_len) {
      best_len = temp_len;
      for (int i=0; i<nNodes; i++) {
        best[i] = nodes[i];
        }
      }
    //for (Node elem : original) cout << elem.coords();
    //  cout << endl;
    } while (next_permutation(indx, indx + nNodes));

  cout << best_len << endl;
  for (Node elem : best) cout << elem.coords();
  cout << endl;

  }






