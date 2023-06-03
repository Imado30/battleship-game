#include <pybind11/pybind11.h>
#include <Schiffe.hpp>


namespace py = pybind11;
using namespace SchiffeVersenken;

PYBIND11_MODULE(schiffeversenken, m) {
    m.doc() = "Schiffe versenken";

    py::class_<Schiffe>(m, "Schiffe")
        .def(py::init<>())
        .def("schiffe_platzieren", &Schiffe::schiffe_platzieren)
        .def("koordinaten_einfügen", &Schiffe::koordinaten_einfügen);
}