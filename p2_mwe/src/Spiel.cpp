//#include "/home/odin/Projekt2/p2_mwe/include/Spiel.hpp"
#include "../include/Spiel.hpp"
#include "../include/Spieler.hpp"

#include <iostream>

namespace SchiffeVersenken{

    Spiel::Spiel(Spieler a, Spieler b):spieler1(a), spieler2(b){
        turn=spieler1.get_id();                 //neu
    };
    
    void Spiel::spielbretter_verbinden(){
        spieler1.set_ene_sb(spieler2.get_own_sb());
        spieler2.set_ene_sb(spieler1.get_own_sb());
    }

    int Spiel::get_turn(){                      //neu
        return turn;
    }
}