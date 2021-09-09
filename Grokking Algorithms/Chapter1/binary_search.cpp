#include <iostream>

int binarySearch(int* arr, size_t size, int num);

int main()
{
	int arr[]{1,3,5,7,9,11};
	size_t arrSize{sizeof(arr)/sizeof(int)};
	std::cout << binarySearch(arr, arrSize, 1) << '\n';
	std::cout << binarySearch(arr, arrSize, 3) << '\n';
	std::cout << binarySearch(arr, arrSize, 5) << '\n';
	std::cout << binarySearch(arr, arrSize, 7) << '\n';
	std::cout << binarySearch(arr, arrSize, 9) << '\n';
	std::cout << binarySearch(arr, arrSize, 11) << '\n';
	std::cout << binarySearch(arr, arrSize, 2) << '\n';

	return 0;
}

int binarySearch(int* arr, size_t size, int num)
{
	size_t low{0};
	size_t high{size - 1};

	while(low <= high)
	{
		size_t mid{(low + high) / 2};
		int guess{arr[mid]};
		if(guess == num)
			return mid;
		if(guess > num)
			high = mid - 1;
		else
			low = mid + 1;
	}

	return -1;
}
