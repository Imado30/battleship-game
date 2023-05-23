#include "/home/odin/Projekt2/p2_mwe/include/Spieler.hpp"
#include <iostream>
#include <functional>

namespace SchiffeVersenken{

    Spieler::Spieler(std::string Name){
        name=Name;
        id=std::hash<std::string>()(Name);
    }

    void Spieler::Schießen(int x, int y){
        if (ene_sb.hit(x, y)){
            markieren(x,y,"X");
            return;
        }
        markieren(x, y, "O");
    }

    void Spieler::markieren(int x,int y, std::string value){
        ene_sb.set_value(x,y,value);
        own_sb.set_value(x,y,value);
        opview.set_value(x,y,value);
    }

}