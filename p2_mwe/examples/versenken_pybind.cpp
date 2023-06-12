#include <pybind11/pybind11.h>
#include <Spieler.hpp>
#include <Lobby.hpp>
#include <Spiel.hpp>
#include <Schiffe.hpp>
#include <pybind11/stl.h>

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
        .def("queue_size", &Lobby::queue_size)
        .def("add_array", &Lobby::add_array)
        .def("array_by_id", &Lobby::array_by_id)
        .def("game_by_id", &Lobby::game_by_id)
        .def("add_t", &Lobby::add_t)
        .def("player_by_id", &Lobby::player_by_id);

    py::class_<Spieler>(m, "Spieler")
        .def(py::init<std::string>())
        .def("get_id", &Spieler::get_id)
        .def("get_ship", &Spieler::get_ship)
        .def("get_in_game", &Spieler::get_in_game)
        .def("set_x", &Spieler::set_x)
        .def("set_y", &Spieler::set_y)
        .def("getx", &Spieler::get_x)
        .def("add_tuple", &Spieler::add_tuple);
        //.def("markieren", &Spieler::markieren)

    py::class_<Spiel>(m, "Spiel")
        .def(py::init<Spieler, Spieler, int>())
        .def("get_turn", &Spiel::get_turn)
        .def("add_tup1", &Spiel::add_tup1)
        .def("add_tup2", &Spiel::add_tup2)
        .def("get_p1", &Spiel::get_p1)
        .def("get_p2", &Spiel::get_p2);

    
    py::class_<Schiffe>(m, "Schiffe")
        .def(py::init<>())
        .def("get_tupel", &Schiffe::get_tupel)
        .def("hit", &Schiffe::hit)
        .def("tupel_erstellen", &Schiffe::tupel_erstellen)
        .def("get_size", &Schiffe::get_size)
        .def("get_koordinaten", &Schiffe::get_koordinaten)
        .def("koordinaten_einfügen", &Schiffe::koordinaten_einfügen);


}