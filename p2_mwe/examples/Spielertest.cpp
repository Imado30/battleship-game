//#include "/home/odin/Projekt2/p2_mwe/include/Spiel.hpp"
//#include "/home/odin/Projekt2/p2_mwe/include/Spieler.hpp"
//#include "/home/odin/Projekt2/p2_mwe/include/Spielbrett.hpp"
#include "../include/Spieler.hpp"
#include "../include/Spiel.hpp"
#include "../include/Spielbrett.hpp"
#include "../src/Spieler.cpp"
#include "../src/Spiel.cpp"
#include "../src/Spielbrett.cpp"



int main(){

    SchiffeVersenken::Spieler a("Christoph");
    SchiffeVersenken::Spieler b("Sangria");

    SchiffeVersenken::Spiel x(a,b);

    x.spielbretter_verbinden();

    a.Schießen(1,2);
    a.Schießen(2,3);

    b.get_own_sb()->druckeSpielbrett();
    a.get_own_sb()->druckeSpielbrett();
}