#pragma once
#include <iostream>
#include "/home/odin/Projekt2/p2_mwe/include/Spieler.hpp"

namespace SchiffeVersenken{

    class Spiel{
        public:
            Spiel(Spieler a, Spieler b);

            void spielbretter_verbinden();

        private:
            Spieler spieler1;
            Spieler spieler2;
    };
}