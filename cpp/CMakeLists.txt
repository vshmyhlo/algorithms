cmake_minimum_required(VERSION 3.13)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

add_executable(main main.cpp)
add_executable(merge_sort sorting/merge_sort.cpp)
