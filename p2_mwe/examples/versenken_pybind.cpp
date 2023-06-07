// uvicorn main:rest_api --port 8000 --reload
// cmake -S . -B build && cmake --build build && cmake --install build
// python3 -m uvicorn main:rest_api --port 8000 --reload

#include <pybind11/pybind11.h>
#include <Schiffe.hpp>


namespace py = pybind11;
using namespace SchiffeVersenken;

PYBIND11_MODULE(schiffeversenken, m) {
    m.doc() = "Schiffe versenken";

    py::class_<Schiffe>(m, "Schiffe")
        .def(py::init<>())
        .def("get_tupel", &Schiffe::get_tupel)
        .def("koordinaten_einfügen", &Schiffe::koordinaten_einfügen);
}