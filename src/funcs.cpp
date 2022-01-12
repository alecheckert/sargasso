#include <sargasso.h>

template <typename T>
T add(T a, T b) {
    return a + b;
}
template int add<int>(int, int);
template float add<float>(float, float);
