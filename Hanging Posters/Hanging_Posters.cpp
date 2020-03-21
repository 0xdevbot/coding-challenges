//
// Created by Devin Wallace on 3/20/20.
//

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'solve' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER h
 *  2. INTEGER_ARRAY wallPoints
 *  3. INTEGER_ARRAY lengths
 */

/*
 * For this challenge I had to write solve(). Please see the description file for more details on the goal.
 * In short I had to take teach item in vector lengths and get 25% of that value.
 * Then subtract that from the corresponding value in vector wallPoints.
 * Next round the result up (IE 11.2 -> 12 & 11.6 -> 12).
 * Finally subtract h (height) from the result.
 * Doing this gave me my min ladder height which was then compared to the current min ladder height.
 * return largest min ladder height.
 */
int solve(int h, vector<int> wallPoints, vector<int> lengths) {
    int min = 0;
    for (int i = 0; i < wallPoints.size(); i++){
        int temp = (ceil(wallPoints[i] - (lengths[i]*.25))) - h;
        if (temp > min) {
            min = int(temp);
        }
    }
    return min;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int h = stoi(first_multiple_input[1]);

    string wallPoints_temp_temp;
    getline(cin, wallPoints_temp_temp);

    vector<string> wallPoints_temp = split(rtrim(wallPoints_temp_temp));

    vector<int> wallPoints(n);

    for (int i = 0; i < n; i++) {
        int wallPoints_item = stoi(wallPoints_temp[i]);

        wallPoints[i] = wallPoints_item;
    }

    string lengths_temp_temp;
    getline(cin, lengths_temp_temp);

    vector<string> lengths_temp = split(rtrim(lengths_temp_temp));

    vector<int> lengths(n);

    for (int i = 0; i < n; i++) {
        int lengths_item = stoi(lengths_temp[i]);

        lengths[i] = lengths_item;
    }

    int answer = solve(h, wallPoints, lengths);

    fout << answer << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
            s.begin(),
            find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
            find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
            s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
