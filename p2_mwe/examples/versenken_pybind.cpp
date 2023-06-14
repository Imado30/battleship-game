// uvicorn Server:rest_api --port 8000 --reload
// cmake -S . -B build && cmake --build build && cmake --install build
// python3 -m uvicorn Server:rest_api --port 8000 --reload

#include <pybind11/pybind11.h>
#include <Schiffe.hpp>
#include <Spieler.hpp>
#include <Lobby.hpp>
#include <Spiel.hpp>
#include <pybind11/stl.h>

namespace py = pybind11;
using namespace SchiffeVersenken;

PYBIND11_MODULE(schiffeversenken, m) {
    m.doc() = "Schiffe versenken";

    py::class_<Schiffe>(m, "Schiffe")
        .def(py::init<>())
        .def("get_tupel", &Schiffe::get_tupel)
        .def("hit", &Schiffe::hit)
        .def("tupel_erstellen", &Schiffe::tupel_erstellen)
        .def("koordinaten_löschen", &Schiffe::koordinaten_löschen)
        .def("get_size", &Schiffe::get_size)
        .def("get_koordinaten", &Schiffe::get_koordinaten)
        .def("set_koordinaten", &Schiffe::set_koordinaten)
        .def("koordinaten_einfügen", &Schiffe::koordinaten_einfügen);

    py::class_<Lobby>(m, "Lobby")
        .def(py::init<>())
        .def("spiel_erstellen", &Lobby::spiel_erstellen)
        .def("spieler_erstellen", &Lobby::spieler_erstellen)
        .def("get_player1", &Lobby::get_player1)
        .def("spiele_size", &Lobby::spiele_size)
        .def("queue_size", &Lobby::queue_size)
        .def("add_array", &Lobby::add_array)
        .def("array_by_id", &Lobby::array_by_id)
        .def("game_by_id", &Lobby::game_by_id)
        .def("add_t", &Lobby::add_t)
        .def("edit_game", &Lobby::edit_game)
        .def("erase_game", &Lobby::erase_game)
        .def("hit", &Lobby::hit)
        .def("player_by_id", &Lobby::player_by_id);

    py::class_<Spieler>(m, "Spieler")
        .def(py::init<std::string>())
        .def("get_id", &Spieler::get_id)
        .def("get_ship", &Spieler::get_ship)
        .def("get_in_game", &Spieler::get_in_game)
        .def("get_gid", &Spieler::get_gid)
        .def("set_gid", &Spieler::set_gid)
        .def("add_tuple", &Spieler::add_tuple);
        //.def("markieren", &Spieler::markieren)

    py::class_<Spiel>(m, "Spiel")
        .def(py::init<Spieler, Spieler, int>())
        .def("get_turn", &Spiel::get_turn)
        .def("add_tup1", &Spiel::add_tup1)
        .def("add_tup2", &Spiel::add_tup2)
        .def("set_turn", &Spiel::set_turn)
        .def("set_over", &Spiel::set_over)
        .def("get_over", &Spiel::get_over)
        .def("get_p1", &Spiel::get_p1)
        .def("get_p2", &Spiel::get_p2);
}