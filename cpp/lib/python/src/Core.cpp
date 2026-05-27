#include <pybind11/pybind11.h>
namespace py = pybind11;
PYBIND11_MODULE(Core, m) {
    m.doc() = "CloudIDE Core Python module";
    m.def("version", []() { return "0.1.0"; });
}
