#pragma once
#include <iostream>
#include "Spieler.hpp"
#include "Spiel.hpp"
#include <vector>

namespace SchiffeVersenken{

    class Lobby{
        public:

            Lobby();

            Spiel spiel_erstellen();

            Spieler spieler_erstellen(std::string name);

            bool waiting(int id);

            Spieler get_player1();

        private:

            std::vector<Spieler> queue;
            std::vector<Spiel> spiele;

    };
}