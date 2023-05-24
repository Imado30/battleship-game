#pragma once
#include <iostream>
#include "../include/Spielbrett.hpp"
//#include "/home/odin/Projekt2/p2_mwe/include/Spielbrett.hpp"
#include <string>
#include <memory>

namespace SchiffeVersenken{

    class Spieler{
    public:
        Spieler(std::string Name);

        void Schießen(int x, int y);

        void markieren(int x, int y, std::string value);

        std::shared_ptr<SpielBrett> get_own_sb();

        void set_ene_sb(std::shared_ptr<SpielBrett> ensb);

    private:
        std::string name;

        size_t id;

        SpielBrett own_sb;

        SpielBrett opview;

        std::shared_ptr<SpielBrett> ene_sb;
    };

}