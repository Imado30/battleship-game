//#include "/home/odin/Projekt2/p2_mwe/include/Spieler.hpp"
#include "../include/Spieler.hpp"
#include <iostream>
#include <functional>
#include <string>

namespace SchiffeVersenken{

    Spieler::Spieler(std::string Name){
        name=Name;
        id=std::hash<std::string>()(Name);
    }

    void Spieler::Schießen(int x, int y){
        if (ene_sb/*->hit(x, y)*/){             // Fehler liegt an hit, wahrscheinlich, weil die membervariablen own_sb und ene_sb keine Spielbretter enthalten, müssten mit Spielbrett initialisiert werden
            //markieren(x,y,"X");
            return;
        }
        //markieren(x, y, "O");
    }

    void Spieler::markieren(int x,int y, std::string value){
        ene_sb->set_value(x,y,value);
        opview.set_value(x,y,value);
    }

    std::shared_ptr<SpielBrett> Spieler::get_own_sb(){
        return std::make_shared<SpielBrett>(own_sb);
    }

    void Spieler::set_ene_sb(std::shared_ptr<SpielBrett> ensb){
        ene_sb=ensb;
    }

    int Spieler::get_id(){
        return id;
    }
}