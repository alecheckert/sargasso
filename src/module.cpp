#include <sargasso.h>

PYBIND11_MODULE(_sargasso, m) {
    m.def("add", &add<int>);
}
