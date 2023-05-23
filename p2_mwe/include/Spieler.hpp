#pragma once
#include <iostream>
#include "/home/odin/Projekt2/p2_mwe/include/Spielbrett.hpp"
#include <string>

namespace SchiffeVersenken{

    class Spieler{
    public:
        Spieler(std::string Name);

        void Schießen(int x, int y);

        void markieren(int x, int y, std::string value);

        SpielBrett& get_own_sb();

        void set_ene_sb(SpielBrett& ensb);

    private:
        std::string name;

        size_t id;

        SpielBrett own_sb;

        SpielBrett ene_sb;

        SpielBrett opview;
    };

}