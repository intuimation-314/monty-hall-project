/**
 * @file main.cpp
 * @brief Entry point for Monty Hall simulation and interactive game.
 *
 * Provides a text-based menu that allows users to:
 * - Play interactive Monty Hall games (3 or custom n doors)
 * - Run simulations to analyze winning strategies
 * - View a log of past results stored in a text file
 */

 #include "monty_hall.h"
 #include <iostream>
 
 using namespace std;
 
 /**
  * @brief Displays the main menu options.
  */
 void showMenu() {
     cout << "\n========= Monty Hall Menu =========\n";
     cout << "1. Play interactive game (3 doors)\n";
     cout << "2. Play interactive game (n doors)\n";
     cout << "3. Run simulation (3 doors)\n";
     cout << "4. Run simulation (n doors)\n";
     cout << "5. View past statistics\n";
     cout << "6. Exit\n";
     cout << "====================================\n";
     cout << "Choose an option (1-6): ";
 }
 
 /**
  * @brief The main function driving user input and flow control.
  *
  * Uses MontyHall class for game logic and stats functions for history.
  * Allows replaying multiple sessions until user exits.
  */
 int main() {
     int choice;
     do {
         showMenu();
         cin >> choice;
 
         if (choice == 1) {
             MontyHall game(3);
             game.runInteractiveGame();
         } else if (choice == 2) {
             int doors;
             cout << "Enter number of doors (minimum 3): ";
             cin >> doors;
             MontyHall game(doors);
             game.runInteractiveGame();
         } else if (choice == 3) {
             int sims;
             cout << "Enter number of simulations: ";
             cin >> sims;
             MontyHall game(3);
             game.runSimulation(sims);
         } else if (choice == 4) {
             int doors, sims;
             cout << "Enter number of doors (minimum 3): ";
             cin >> doors;
             cout << "Enter number of simulations: ";
             cin >> sims;
             MontyHall game(doors);
             game.runSimulation(sims);
         } else if (choice == 5) {
             viewGameStats();
         } else if (choice == 6) {
             cout << "Goodbye!\n";
         } else {
             cout << "Invalid choice. Try again.\n";
         }
 
     } while (choice != 6);
 
     return 0;
 }