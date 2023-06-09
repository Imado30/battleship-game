#pragma once
#include <iostream>
#include "../include/Spieler.hpp"


namespace SchiffeVersenken{

    class Spiel{
        public:
            Spiel(Spieler a, Spieler b, int id);

            void spielbretter_verbinden();

            int get_turn();

            int get_game_id();

        private:
            Spieler spieler1;
            Spieler spieler2;
            int turn;
            int game_id;
    };
}