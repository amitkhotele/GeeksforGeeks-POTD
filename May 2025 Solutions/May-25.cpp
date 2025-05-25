class Solution {
public:
    bool pythagoreanTriplet(vector<int>& arr) {
        unordered_set<int> squareSet;
        int n = arr.size();

        // Insert all squares into set
        for (int i = 0; i < n; ++i) {
            squareSet.insert(arr[i] * arr[i]);
        }

        // Try every pair (a, b) and check if a^2 + b^2 exists in set
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int sum = arr[i]*arr[i] + arr[j]*arr[j];
                if (squareSet.find(sum) != squareSet.end()) {
                    return true;
                }
            }
        }

        return false;
    }
};
