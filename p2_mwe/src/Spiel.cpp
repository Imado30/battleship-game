//#include "/home/odin/Projekt2/p2_mwe/include/Spiel.hpp"
#include "../include/Spiel.hpp"
#include "../include/Spieler.hpp"

#include <iostream>

namespace SchiffeVersenken{

    Spiel::Spiel(Spieler a, Spieler b, int id):spieler1(a), spieler2(b){
        turn=spieler1.get_id();                 //neu
        game_id=id;
        a.set_in_game(id);
        b.set_in_game(id);
        over=false;
    };
   /* 
    void Spiel::spielbretter_verbinden(){
        spieler1.set_ene_sb(spieler2.get_own_sb());
        spieler2.set_ene_sb(spieler1.get_own_sb());
    }
*/
    int Spiel::get_turn(){                      //neu
        return turn;
    }

    int Spiel::get_game_id(){
        return game_id;
    }

    Spieler Spiel::get_p1(){
        return spieler1;
    }

    Spieler Spiel::get_p2(){
        return spieler2;
    }

    void Spiel::add_tup1(int x, int y){
        spieler1.add_tuple(x,y);
    }

    void Spiel::add_tup2(int x, int y){
        spieler2.add_tuple(x,y);
    }

    void Spiel::set_turn(){
        if (turn==spieler1.get_id()){
            turn=spieler2.get_id();
        }
        else{
            turn=spieler1.get_id();
        }
    }

    void Spiel::set_over(){
        over=true;
    }

    bool Spiel::get_over(){
        return over;
    }
}