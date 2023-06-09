#pragma once
#include <iostream>
#include "Spieler.hpp"
#include "Spiel.hpp"
#include <vector>
#include <map>

namespace SchiffeVersenken{

    class Lobby{
        public:

            Lobby();

            Spiel spiel_erstellen();

            Spieler spieler_erstellen(std::string name);

            bool waiting(int id);

            Spieler get_player1();

            int spiele_size();

            int queue_size();

            Spieler player_by_id(int id);

        private:

            void add_ids();

            std::vector<Spieler> queue;
            //std::vector<Spiel> spiele;
            std::map<int, Spiel> games;
            std::vector<int> game_ids;
            int id_max;
            std::map<int, Spieler> playing;

    };
}