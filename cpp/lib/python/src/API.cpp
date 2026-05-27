#include <pybind11/pybind11.h>
namespace py = pybind11;
PYBIND11_MODULE(API, m) {
    m.doc() = "CloudIDE API Python module";
    m.def("version", []() { return "0.1.0"; });
}
