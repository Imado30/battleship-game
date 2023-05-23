#pragma once
#include <iostream>

namespace SchiffeVersenken{

    class Spieler{
    public:
        Spieler(std::string Name);

        void Schießen(int x, int y);

        void markieren(int x, int y, std::string value);

    private:
        std::string name;

        size_t id;

        Spielbrett own_sb;

        Spielbrett ene_sb;

        Spielbrett opview;
    };

}