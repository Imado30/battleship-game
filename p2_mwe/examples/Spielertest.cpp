#include "../include/Spieler.hpp"
#include "../include/Spiel.hpp"
#include "../include/Spielbrett.hpp"
//#include "../src/Spieler.cpp"
//#include "../src/Spiel.cpp"
//#include "../src/Spielbrett.cpp"

//cmake -S. -B build
//cmake --build build
// ./build/Spielertest.cpp

int main(){

    SchiffeVersenken::Spieler a("A");
    SchiffeVersenken::Spieler b("B");

    SchiffeVersenken::Spiel x(a,b);

    x.spielbretter_verbinden();

    a.Schießen(1,2);
    a.Schießen(2,3);

    //b.get_own_sb()->druckeSpielbrett();
    //a.get_own_sb()->druckeSpielbrett();
}