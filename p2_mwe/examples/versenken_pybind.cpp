#include <pybind11/pybind11.h>
#include <Spieler.hpp>

namespace py = pybind11;
using namespace SchiffeVersenken;

PYBIND11_MODULE(schiffeversenken, m) {
  m.doc() = "Schiffe versenken";

  py::class_<Spieler>(m, "Spieler")
    .def(py::init<std::string>())
    .def("Schießen", &Spieler::Schießen)
    .def("get_own_sb", &Spieler::get_own_sb)
    .def("set_ene_sb", &Spieler::set_ene_sb);
    //.def("markieren", &Spieler::markieren)
}