#include "/home/odin/Projekt2/p2_mwe/include/Spiel.hpp"
#include <iostream>

namespace SchiffeVersenken{

    Spiel::Spiel(Spieler a, Spieler b){
        spieler1=a;
        spieler2=b;
    };
    
    void Spiel::spielbretter_verbinden(){
        spieler1.set_ene_sb(spieler2.get_own_sb());
        spieler2.set_ene_sb(spieler1.get_own_sb());
    }
}