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

int main(int argc, const char* argv[]) {
return 0;
}
