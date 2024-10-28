#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;

    int count = 0;
    char block, before, next;

    cin.ignore();
    cin.get(block);
    before = block;

    for (int i = 0; i < N - 1; i++) {
        cin.get(next);

        if (block != before) {
            count++;
            if (next == before) {
                block = before;
            }
        }

        before = block;
        block = next;
    }

    if (before != block || next == 'B') {
        count++;
    }

    cout << count << endl;

    return 0;
}