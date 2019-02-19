//
// Created by Vlad Shmyhlo on 2019-01-08.
//

#include <vector>
#include <iostream>
#include <algorithm>

// TODO: init aux once


template<typename T>
void merge(std::vector<T> &xs, size_t lo, size_t mid, size_t hi) {
    std::vector<T> tmp(hi - lo);

    size_t i = lo;
    size_t j = mid;
    size_t k = 0;

    while (i < mid && j < hi) {
        if (xs[i] < xs[j]) {
            tmp[k] = xs[i];
            i++;
        } else {
            tmp[k] = xs[j];
            j++;
        }

        k++;
    }


    while (i < mid) {
        tmp[k] = xs[i];
        i++;
        k++;
    }

    while (j < hi) {
        tmp[k] = xs[j];
        j++;
        k++;
    }

    for (int i = 0; i < hi - lo; i++) {
        xs[lo + i] = tmp[i];
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

