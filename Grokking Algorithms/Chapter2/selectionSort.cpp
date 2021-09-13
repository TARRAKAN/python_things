#include <iostream>
#include <vector>

size_t findSmallest(std::vector<int> arr)
{
	int smallest{arr[0]};
	size_t smallestIndex{0};
	for(size_t i{1}; i < arr.size(); i++)
	{
		if(arr[i] < smallest)
		{
			smallest = arr[i];
			smallestIndex = i;
		}
	}
	return smallestIndex;
}

std::vector<int>* selectionSort(std::vector<int> arr)
{
	std::vector<int>* newArr = new std::vector<int>;
	size_t size{arr.size()};
	for(size_t i{0}; i < size; i++)
	{
		size_t smallest{findSmallest(arr)};
		newArr->push_back(arr[smallest]);
		arr.erase(arr.begin()+smallest);
	}
	return newArr;
}

int main()
{
	std::vector<int>array{6,5,7,4,8,3,10,9,2,1};
	std::vector<int>* sortedArray{selectionSort(array)};
	for(int num: *sortedArray)
	{
		std::cout << num <<", ";
	}
	std::cout << std::endl;
	delete sortedArray;
	return 0;
}
