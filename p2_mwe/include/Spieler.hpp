#pragma once
#include <iostream>

namespace SchiffeVersenken{

    class Spieler{
    public:
        Spieler(std::string Name);

        void Schießen(int Koord1, int Koord2);

        bool hit_or_miss(int Koord1, int Koord2);

        void markieren(int Koord1, int Koord2);

    private:
        std::string name;

        size_t id;
    };

}