#include <bits/stdc++.h>
#define int long long
#define MAX_DAILY_ORDERS 30 
using namespace std;


int32_t main(){

    // this file contains the dates (represented as integers) of orders and codes
    fstream filein("./kindabackend/coded_orders.txt");

    //this file will store the output of the optimization for each number of days
    ofstream fileout("./kindabackend/res.txt");


    // take the input as a vector of pairs
    int n_orders;
    filein >> n_orders;
    vector <pair <int, int>> orders(n_orders);
    for (int element = 0; element < n_orders; element++){
        filein >> orders[element].first >> orders[element].second;
    }

    // sorting in order to apply dp later
    sort(orders.begin(), orders.end());

    // 2d dynamic programming tables keeping min delay and the set of days in order to achieve it 

    // in general it follows DP[last_processed_order][number_of_distinct_days] = minimum_achievable_sum_of_delays

    vector <vector <int>> min_delay(n_orders + 1, vector <int> (n_orders + 1, INT_MAX)); 
    vector <vector <set <int>>> days(n_orders + 1, vector <set <int>> (n_orders + 1));

    for (int j = 0; j < n_orders; j++){
        min_delay[0][j] = 0;
    }


    // updating the dp table, the transition is:
    // dp[i][j] = min (dp[element][n_days], dp[previous_element][n_days-1] + delay_of_new) over all previous elements which i can take

    for (int element = 1; element <= n_orders; element++){
        for (int n_days = 1; n_days <= n_orders; n_days++){
            int partial_delay = 0;

            for (int previous_element = element - 1; previous_element >= 0 && previous_element >= element - MAX_DAILY_ORDERS; previous_element--){

                // if i get a better result i update both the delay and the days in order to achieve it
                if (min_delay[element][n_days] > min_delay[previous_element][n_days-1] + partial_delay){

                    min_delay[element][n_days] = min_delay[previous_element][n_days-1] + partial_delay;
                    days[element][n_days] = days[previous_element][n_days-1];

                }
                partial_delay += orders[element-1].first - orders[previous_element-1].first;
            }
            days[element][n_days].insert(orders[element-1].first);
        }
    }

    // this part is just for putting the results in res.txt
        for (int j=0; j<= n_orders; j++){
            if (min_delay[n_orders][j]==INT_MAX){
                fileout << -1;
            }
            else{
                fileout << min_delay[n_orders][j] << ' ';
                for (auto x:orders){
                    fileout << x.second << ' ';
                    fileout << x.first << ' ' << *days[n_orders][j].lower_bound(x.first) << "    ";
                }

            }
            fileout << endl;
        }


        return 0;
}