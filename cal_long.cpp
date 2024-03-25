#include<bits/stdc++.h>
using namespace std;

// CONSTANTS
double k; //spring constant
double o; //original length
int n;   //number of particles
double mass; //mass of particles

double a;//amplitude
double f; // frequency

int fps; // frames per second
int t;// time

inline void input(){
    freopen("config_long.txt","r",stdin);
    string tmp;
    cin>>k>>tmp;
    cin>>o>>tmp;
    cin>>n>>tmp;
    cin>>mass>>tmp;
    cin>>a>>tmp;
    cin>>f>>tmp;
    cin>>fps>>tmp;
    cin>>t>>tmp;
    cout<<k<<','<<o<<','<<n<<','<<mass<<','<<a<<','<<f<<','<<fps<<','<<t<<endl;
    fclose(stdin);
}
// END

const double PI = 3.1415926535897932384;

vector<double> x; // position of particles
vector<double> nx;// new position
vector<vector<double> > res; // result
vector<double> force,v,bv;
inline void init(){
    input();
    for(int i=0;i<n;i++){
        x.push_back(o*i);
        nx.push_back(0);
        force.push_back(0);
        v.push_back(0);
        bv.push_back(0);
    }
}
bool WARNING;
inline void algorithm(){
    res.push_back(x);
    double dt = 1.0 / fps; // delta time
    for(int i = 1;i<fps*t;i++){
        for(int p = 1;p<n;p++){//calculate the force,velocity and displacement
            force[p] = -k * (abs(x[p] - x[p-1])-o) * (x[p] > x[p-1]?1:-1);
            if(p != n-1){//not the end
                force[p] += k * (abs(x[p+1]-x[p])-o) * (x[p+1] > x[p]?1:-1);
            }
            if(x[p]<x[p-1] && WARNING == false){
                cout<<"WARNING!"<<endl;
                WARNING = true;
            }
            v[p] = bv[p] + force[p]*dt/mass;
            nx[p] = x[p] + (bv[p] + v[p]) / 2.0 * dt;
        }
        nx[0] = a * sin(i*dt*f*PI);
        res.push_back(nx);
        x = nx;
        bv = v;
    }
}
inline void output(){
    freopen("positions_long.txt","w",stdout);
    cout<<fps<<" "<<t<<endl;
    for(auto i:res){
        for(auto j:i){
            printf("%.3lf ",j);
        }
        cout<<endl;
    }
    fclose(stdout);
}
int main(){
    init();
    algorithm();
    output();
}
