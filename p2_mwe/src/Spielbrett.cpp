#include <vector>
#include <string>
#include <iostream>
//#include "/home/odin/Projekt2/p2_mwe/include/Spielbrett.hpp"
#include "../include/Spielbrett.hpp"

using namespace std;

namespace SchiffeVersenken {

SpielBrett::SpielBrett() {
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            Feld[i][j] = "-";
        }
    }
}

void SpielBrett::druckeSpielbrett() {
  //Zahlen 0-9 drucken

    cout<<"  ";

    for (int i = 0; i<10; i++){
      cout << i << " ";
    }

    cout <<endl;

    cout<<"  ";

    for (int i = 0; i<10; i++){
      cout <<"- ";
    }
    cout<<endl;
      
    for (int i = 0; i < 10; i++) {
      cout << i << "|";     // idrucken und | 
        for (int j = 0; j < 10; j++) {
            std::cout << Feld[i][j] <<  " ";
        }
        std::cout << std::endl;
    }

  
}
    
    
void SpielBrett::set_value(int x, int y, string s){
Feld[x][y] = s;
}

bool SpielBrett::hit(int x, int y){

  if (Feld[x][y] == "<" || ">"){
    return true;
    } 
  else 
    return false;

}
}