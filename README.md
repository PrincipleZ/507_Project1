# Card Game "War" Simulator

This is a python program that will simulate the card game "War". 

## Getting Started

Clone the code and run ```python3 SI507F17_project1_cards.py``` to begin the simulation.

### Prerequisites

Required packages to run the program are included in the requirements.txt
Use ```pip install -r requirements.txt``` to install the required packages.

## Code function

#### A class ```Card```
* The class Card has 3 class variables: ```suit_names```, ```rank_levels```, and ```faces```
* ```suit_names``` contains a list of strings that represent suits: ```Diamonds```, ```Clubs```, ```Hearts```, ```Spades```
* ```rank_levels``` contains a list of integers, 1-13
* ```faces``` contains a dictionary whose keys are numbers and whose values are strings. It has the following key-value pairs:
    * 1:"Ace"
    * 11:"Jack"
    * 12:"Queen"
    * 13:"King"

* The class ```Card```'s constructor accepts a number representing a suit and a number representing a rank. Do not put in a number that is an invalid suit (less than zero or greater than 3) or an invalid rank (less than zero or greater than 13). The default value for a suit in the Card constructor is 0, for Diamonds, and the default value for the rank in the Card constructor is 2.

* The ```Card``` constructor will assign the following instance variables:
    * ```self.suit```, to hold the string name representing the suit of the card
    * ```self.rank```, to hold EITHER the number or the string representation as appropriate of the card rank (so if a card is created with rank 12, its self.rank should be "Queen", etc)
    * ```self.rank_num```, to hold the NUMBER representing the rank (this value should always be an integer)

* The ```Card``` class has a string method, called by ```str(a)``` where a is an instance of ```Card```.
It will return a string representing the card. e.g. "Ace of Spades" or "3 of Clubs", etc.

#### A class ```Deck```
* The class Deck's constructor does not accept input, and you can assume this will always be handled correctly by a programmer using this code.

* The Deck constructor builds a list of cards -- all the cards that would be included in a 52-card deck: rank 1-13 of each of the four suits.

* The Deck constructor creates one instance variable: self.cards, which should hold a list of Card objects when a Deck instance is created.

* The Deck string method should return a multi-line string with one line for each printed representation of a card in the deck. So a complete deck should have a 52-line string of strings like "Ace of Diamonds", "Two of Diamonds", etc.

* Deck has a method pop_card which accepts an integer as input and has a default value such that the Deck will pop off the last (top) card of the deck, as if you're taking off the top card in a card game. When pop_card is invoked on a Deck instance, the last card in the deck is removed from the deck. You should be able to "pop" all of the cards off of the deck until the deck is empty (its self.cards list is the empty list).

* Deck has a method shuffle which accepts no external input and shuffles the self.cards list in the Deck at that time so that it has a random order.

* Deck has a method replace_card which accepts a Card instance as input. If the card instance input into the method is NOT already in the deck, it is added back to the deck. If it IS already in the deck, nothing changes about the Deck (a deck should not have any duplicate cards as a result of calling this method).

* Deck has a method sort_cards which should organize the cards remaining in the deck into an order such that they are in ascending order by suit: Diamonds, then Clubs, then Hearts, then Spades.

* Deck has a method deal_hand which takes a required input hand_size, an integer representing the number of cars in the hand. It should return a list of Card objects that make up the hand dealt. A hand should be able to be dealt up to the full size of the current deck (e.g. if 3 cards have been removed from the deck and not replaced, it should be impossible to deal a 52-card hand, but if no cards have been removed, it should be possible)

## Running the tests

The test can be run by ```python3 SI507F17_project1_tests.py``` from command line.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### Coding style

This project follows PEP8 style.


## Acknowledgments

* This project is the first homework project for SI507 at University of Michigan. Any bugs in the code was intentionally written.

