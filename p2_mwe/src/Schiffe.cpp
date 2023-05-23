#include "../include/Schiffe.hpp"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
namespace SchiffeVersenken
{
    Schiffe::Schiffe()
    {
        Schiffgrößen.push_back(6);
        Schiffgrößen.push_back(5);
        Schiffgrößen.push_back(4);
        Schiffgrößen.push_back(3);
        Schiffgrößen.push_back(2);
    }

    void Schiffe::schiffe_platzieren()
    {
        while (Schiffgrößen.size() != 0)
        {
            // geordnetes Schiffgrößen Array wird nach jeder Eingabe dem Spieler vorgezeigt
            std::sort(std::begin(Schiffgrößen), std::end(Schiffgrößen), std::greater<>());

            cout << "Es stehen dir folgende Schiffgrößen zum platzieren zur Verfügung: [ ";
            for (int i = 0; i < Schiffgrößen.size(); i++)
            {
                cout << Schiffgrößen[i] << " ";
            }
            cout << "]" << endl << "Gebe die Schiffgröße an, mit der du anfangen willst                                 (0 ist der Reset Button, falls du alles neu anordnen willst)" << endl;

            // Eingabe der Schiffgröße
            int eingabe;
            cin >> eingabe;
            cout << endl;

            // 0 wäre der Reset Button
            if (eingabe != 0)
            {
                //neues Array wo eingabe und die restlichen Schiffgrößen eingefügt und sortiert werden
                vector<int> überprüfen;
                überprüfen.push_back(eingabe);
                for (int i = 0; i < Schiffgrößen.size(); i++)
                {
                    if (Schiffgrößen[i] != eingabe)
                        überprüfen.push_back(Schiffgrößen[i]);
                }
                std::sort(std::begin(überprüfen), std::end(überprüfen), std::greater<>());

                // Es wird auf gleichheit der Arrays überprüft. Ist die Eingabe keine Zahl aus den Schiffgrößen, sind die Arrays ungleich => Exception
                if (überprüfen == Schiffgrößen)
                {
                    //Hier müssen noch überall exceptions hin!!!
                    int x_koordinate;
                    int y_koordinate;
                    string richtung;
                    cout << "Gib die x-Koordinate ein für Schiff Größe " << eingabe << endl;
                    cin >> x_koordinate;
                    cout << "Gib die y-Koordinate ein für Schiff Größe " << eingabe << endl;
                    cin >> y_koordinate;
                    cout << "gib h für horizontal und v für vertikal ein " << endl;
                    cin >> richtung;

                    //Schiffe::koordinaten_einfügen(eingabe, x_koordinate, y_koordinate, richtung);

                    //Die Eingabe wird durch Positionen tauschen im Array aus Schiffgrößen entfernt und in anderes Array eingefügt
                    for (int i = 0; i < Schiffgrößen.size(); i++)
                    {
                        if (Schiffgrößen[i] == eingabe)
                        {
                            Schiffgrößen2.push_back(Schiffgrößen[i]);
                            int last_element = Schiffgrößen[Schiffgrößen.size()-1];
                            int current_element = Schiffgrößen[i];
                            Schiffgrößen[i] = last_element;
                            Schiffgrößen[Schiffgrößen.size()] = current_element;
                            Schiffgrößen.pop_back();

                            //überprüfen Array muss geleert werden
                            for (int i = 0; i < überprüfen.size(); i++)
                            {
                                überprüfen.pop_back();
                            }
                        }
                    }
                }
                else 
                {
                    throw std::invalid_argument ("Eingegebenes Element gehört nicht zu den Schiffsgrößen");
                }
            }
            /*else 
            {
                Schiffe::reset();
            }*/
        }
    }
}