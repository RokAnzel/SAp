#include <fstream>
#include <vector>
using namespace std;

bool Branje_Stevil(vector<int>& vec, const char s[]) {
	ifstream input(s);
	int st;

	if (!input.is_open()) {
		return false;
	}

	while (!input.eof()) {
		input >> st;
		vec.push_back(st);
		while (isspace(input.peek())) input.get();
	}
	input.close();
	return true;
}

void Izpis_Stevil(int* polje, unsigned int velikost) {
	ofstream output("out.txt");

	for (int i = 0; i < velikost; i++)
		output << polje[i] << ' ';
}

int main(int argc, const char* argv[]) {
<<<<<<< HEAD
	vector<int> A;

	if (argc < 3) return 0;
	if (!Branje_Stevil(A, argv[2])) return 0;

	if (argv[1][0] == '0') {
		int min = 0;
		int max = A[0];
		for (int i = 0; i < A.size(); i++) {
			if (min > A[i]) {
				min = A[i];
			}
		}
		for (int i = 0; i < A.size(); i++) {
			A[i] = A[i] + (min * (-1));
		}

		for (int i = 0; i < A.size(); i++) {
			if (max < A[i]) {
				max = A[i];
			}
		}
		vector<int> C(max + 1);
		for (int i = 0; i < A.size(); i++) {
			C[A[i]] = C[A[i]] + 1;
		}
		for (int i = 1; i < C.size(); i++) {
			C[i] = C[i] + C[i - 1];
		}
		vector<int> B(A.size());
		for (int i = A.size() - 1; i > -1; i--) {
			B[C[A[i]] - 1] = A[i];
			C[A[i]] = C[A[i]] - 1;
		}

		for (int i = 0; i < B.size(); i++) {
			B[i] = B[i] + min;
		}

		A = B;
	}
	else {
		int min = 0;
		int max = A[0];
		for (int i = 0; i < A.size(); i++) {
			if (min > A[i]) {
				min = A[i];
			}
		}
		for (int i = 0; i < A.size(); i++) {
			A[i] = A[i] + (min * (-1));
		}

		for (int i = 0; i < A.size(); i++) {
			if (max < A[i]) {
				max = A[i];
			}
		}
		vector<int> C(max + 1);
		for (int i = 0; i < A.size(); i++) {
			C[A[i]] = C[A[i]] + 1;
		}
		vector<int> B;
		for (int i = 0; i < C.size(); i++) {
			if (C[i] > 0) {
				for (int j = 0; j < C[i]; j++) {
					B.push_back(i);
				}
			}
		}

		for (int i = 0; i < B.size(); i++) {
			B[i] = B[i] + min;
		}
		A = B;
	}
	Izpis_Stevil(&A[0], A.size());

	return 0;
=======
return 0;
>>>>>>> ceaa7a7cff77de3deab9a97a4cc4fec96edde5b0
}
