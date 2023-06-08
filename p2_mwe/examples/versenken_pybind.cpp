#include <pybind11/pybind11.h>
#include <Spieler.hpp>
#include <Lobby.hpp>
#include <Spiel.hpp>

namespace py = pybind11;
using namespace SchiffeVersenken;

PYBIND11_MODULE(schiffeversenken, m) {
    m.doc() = "Schiffe versenken";

    py::class_<Lobby>(m, "Lobby")
        .def(py::init<>())
        .def("spiel_erstellen", &Lobby::spiel_erstellen)
        .def("spieler_erstellen", &Lobby::spieler_erstellen)
        .def("waiting", &Lobby::waiting)
        .def("get_player1", &Lobby::get_player1)
        .def("spiele_size", &Lobby::spiele_size)
        .def("queue_size", &Lobby::queue_size);

    py::class_<Spieler>(m, "Spieler")
        .def(py::init<std::string>())
        .def("Schießen", &Spieler::Schießen)
        .def("get_own_sb", &Spieler::get_own_sb)
        .def("set_ene_sb", &Spieler::set_ene_sb)
        .def("get_id", &Spieler::get_id);
        //.def("markieren", &Spieler::markieren)

    py::class_<Spiel>(m, "Spiel")
        .def(py::init<Spieler, Spieler>())
        .def("spielbretter_verbinden", &Spiel::spielbretter_verbinden);
}