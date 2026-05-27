#include <pybind11/pybind11.h>
namespace py = pybind11;
PYBIND11_MODULE(Nodes, m) {
    m.doc() = "CloudIDE Nodes Python module";
    m.def("version", []() { return "0.1.0"; });
}
