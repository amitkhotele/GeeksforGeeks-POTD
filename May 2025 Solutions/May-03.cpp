class Solution {
  public:

    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    int findNearestPrime(int num) {
        int lower = num, upper = num;
        while (true) {
            if (isPrime(lower)) return lower;
            if (isPrime(upper)) return upper;
            lower--;
            upper++;
        }
    }

    Node *primeList(Node *head) {
        Node* curr = head;
        while (curr != nullptr) {
            curr->val = findNearestPrime(curr->val);
            curr = curr->next;
        }
        return head;
    }
};
