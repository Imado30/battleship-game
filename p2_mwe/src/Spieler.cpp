//#include "/home/odin/Projekt2/p2_mwe/include/Spieler.hpp"
#include "../include/Spieler.hpp"
#include <iostream>
#include <functional>
#include <string>

namespace SchiffeVersenken{

    Spieler::Spieler(std::string Name){
        name=Name;
        id=std::hash<std::string>()(Name);
        in_game=-1;
    }

/*
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
*/
    int Spieler::get_id(){
        return id;
    }

    void Spieler::set_in_game(int id){
        in_game=id;
    }

    int Spieler::get_in_game(){
        return in_game;
    }

    Schiffe Spieler::get_ship(){
        return ship;
    }

    void Spieler::add_tuple(int x, int y){
        ship.tupel_erstellen(x,y);
    }
}