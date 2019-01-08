//
// Created by Vlad Shmyhlo on 2019-01-08.
//

#include <vector>
#include <iostream>
#include <algorithm>

template<typename T>
void merge(std::vector<T> &xs, size_t lo, size_t mid, size_t hi) {
    std::vector<T> left(mid - lo);
    std::vector<T> right(hi - mid);

    for (size_t i = 0; i < mid - lo; i++) {
        left[i] = xs[lo + i];
    }

    for (size_t i = 0; i < hi - mid; i++) {
        right[i] = xs[mid + i];
    }

    size_t i = 0;
    size_t j = 0;
    size_t k = lo;

    while (i < mid - lo && j < hi - mid) {
        if (left[i] < right[j]) {
            xs[k] = left[i];
            i++;
        } else {
            xs[k] = right[j];
            j++;
        }

        k++;
    }


    while (i < mid - lo) {
        xs[k] = left[i];
        i++;
        k++;
    }

    while (j < hi - mid) {
        xs[mid + j] = right[j];
        j++;
        k++;
    }
}


template<typename T>
void merge_sort(std::vector<T> &xs, size_t lo, size_t hi) {
    if (hi - lo <= 1) {
        return;
    }

    size_t mid = lo + (hi - lo) / 2;
    merge_sort(xs, lo, mid);
    merge_sort(xs, mid, hi);
    merge(xs, lo, mid, hi);
}

template<typename T>
void merge_sort(std::vector<T> &xs) {
    merge_sort<T>(xs, 0, xs.size());
}


int main() {
    std::vector<int> xs{5, 9, 6, 8, 0, 1, 7, 3, 2, 4};
    merge_sort(xs);

    for (auto i : xs) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}

