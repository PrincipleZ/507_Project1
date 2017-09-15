# Do not change import statements.
import unittest
import copy
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description
# file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail. 
# If more than 3 tests fail, it should be because multiple of the test methods 
# address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should 
# try to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########


# Test Card class
class testCardClass(unittest.TestCase):
	# Test Card class constructor
	def test_default_constructor(self):
		default_card = Card()
		self.assertEqual(default_card.suit, "Diamonds")
		self.assertEqual(default_card.rank, 2)
		self.assertEqual(default_card.rank_num, 2)
	
	def test_number_constructor1(self):
		six_of_spades = Card(3, 6)
		three_of_hearts = Card(2, 3)
	
		self.assertEqual(six_of_spades.suit, "Spades")
		self.assertEqual(six_of_spades.rank, 6)
		self.assertEqual(three_of_hearts.suit, "Hearts")
		self.assertEqual(three_of_hearts.rank, 3)

	def test_number_constructor2(self):
		five_of_clubs = Card(1, 5)
		eight_of_diamonds = Card(0, 8)

		self.assertEqual(five_of_clubs.suit, "Clubs")
		self.assertEqual(five_of_clubs.rank, 5)
		self.assertEqual(eight_of_diamonds.suit, "Diamonds")
		self.assertEqual(eight_of_diamonds.rank, 8)

	def test_face_constuctor1(self):
		jack_of_diamonds = Card(0, 11)
		queen_of_spades = Card(3, 12)

		self.assertEqual(jack_of_diamonds.rank, "Jack")
		self.assertEqual(jack_of_diamonds.rank_num, 11)
		self.assertEqual(queen_of_spades.rank, "Queen")
		self.assertEqual(queen_of_spades.rank_num, 12)

	def test_face_constructor2(self):
		ace_of_spades = Card(3, 1)
		king_of_hearts = Card(2, 13)

		self.assertEqual(ace_of_spades.rank, "Ace")
		self.assertEqual(ace_of_spades.rank_num, 1)
		self.assertEqual(king_of_hearts.rank, "King")
		self.assertEqual(king_of_hearts.rank_num, 13)

	# Test Card string output
	def test_card_string(self):
		ace_of_spades = Card(3, 1)
		five_of_hearts = Card(2, 5)

		self.assertEqual(str(ace_of_spades), "Ace of Spades", "Output should be Ace of Spades")
		self.assertEqual(str(five_of_hearts), "Five of Hearts")

# Test Deck Class
class testDeckClass(unittest.TestCase):
	def setUp(self):
		self.d = Deck()
	# Test Deck constructor
	def test_deck_constructor(self):
		self.assertEqual(len(self.d.cards), 52)
		# check for duplicates
		card_list = []
		for i in self.d.cards:
			card_list.append(i.suit+" "+str(i.rank))
		self.assertEqual(len(card_list), len(set(card_list)))

	# Not checking contents since it just calls str function for each card
	def test_deck_string(self):
		temp = str(self.d)
		self.assertEqual(temp.count("\n"), 51)

	def test_pop_one_card(self):
		test_list = self.d.cards
		self.d.pop_card()
		test_list.pop(-1)
		self.assertEqual(self.d.cards, test_list)

	def test_pop_all_card(self):
		while self.d.cards:
			self.d.pop_card()
		self.assertFalse(self.d.cards)

	def test_pop_empty(self):

		self.d.cards = []
		
		with self.assertRaises(IndexError):
			self.d.pop_card()

	# A helper function determine if two decks have high similarity. Two decks are considered different
	# if there are more or equal to *th* cards are in different order

	def difference_in_deck(self, a, b, th):
		count = 0
		for i, j in zip(a, b):
			if i.suit != j.suit:
				count += 1
			elif i.rank != j.rank:
				count += 1 
		return count >= th

	def test_shuffle(self):
		d2 = Deck()
		temp = copy.deepcopy(self.d.cards)
		self.d.shuffle()
		d2.shuffle()
		self.assertTrue(self.difference_in_deck(temp, self.d.cards, 10))
		self.assertTrue(self.difference_in_deck(self.d.cards, d2.cards, 10))

	def test_replace_card(self):
		self.d.shuffle()
		temp = copy.deepcopy(self.d.cards)
		card1 = self.d.cards.pop()
		card2 = self.d.cards.pop()
		self.d.replace_card(card2)
		self.assertTrue(len(self.d.cards), 51)
		self.d.replace_card(card1)
		self.assertTrue(len(self.d.cards), 52)
		self.assertFalse(self.difference_in_deck(self.d.cards, temp, 1))

	def test_replace_more_card(self):
		self.d.shuffle()
		temp = copy.deepcopy(self.d.cards)
		card1 = self.d.cards[0]
		card2 = self.d.cards[1]
		self.d.replace_card(card1)
		self.assertTrue(len(self.d.cards), 52)
		self.d.replace_card(card2)
		self.assertTrue(len(self.d.cards), 52)
		self.assertFalse(self.difference_in_deck(temp, self.d.cards, 1))

	def test_sort_cards(self):
		temp = copy.deepcopy(self.d.cards)
		self.d.shuffle()
		self.d.sort_cards()
		self.assertFalse(self.difference_in_deck(temp, self.d.cards, 1))

	def test_deal_full_hand(self):
		temp = copy.deepcopy(self.d.cards)
		self.assertEqual(len(self.d.deal_hand(52)), 52)

	def test_deal_one_card(self):
		self.assertEqual(len(self.d.deal_hand(1)), 1)

	def test_deal_more_than_deck(self):
		self.d.pop_card()
		with self.assertRaises(IndexError):
			self.d.deal_hand(52)

class testWarGame(unittest.TestCase):
	def test_war_game_type(self):
		i = 100
		while i > 0:
			res = play_war_game(testing=True)
			self.assertTrue(type(res) is tuple)
			self.assertTrue(type(res[0]) is str)
			self.assertTrue(type(res[1]) is int)
			self.assertTrue(type(res[2]) is int)
			i -= 1

	def test_war_game_result(self):
		i = 100
		while i > 0:
			res = play_war_game(testing=True)
			if res[0] == "Player1":
				self.assertTrue(res[1] > res[2])
			elif res[0] == "Player2":
				self.assertTrue(res[1] < res[2])
			elif res[0] == "Tie":
				self.assertTrue(res[1] == res[2])
			else:
				self.fail("Game winner should be one of the following: Player1, Player2, Tie")
			i -= 1

class testShowSong(unittest.TestCase):
	def test_show_song_input_type(self):
		with self.assertRaises(TypeError, "There should be a TypeError if input is not a string"):
			show_song([2, 3])

	def test_show_song_return_type(self):
		test_song = show_song()
		self.assertTrue(type(test_song)==helper_functions.Song)

	def test_show_song_search(self):
		test_song = show_song("Poker face")
		songs_resp = helper_functions.get_and_cache_songs("Poker face")
		song_objs = [helper_functions.Song(s) for s in songs_resp["results"]]
		self.assertTrue(test_song in song_objs, "Searching mechanism is not working correctly")



if __name__ == "__main__":
	unittest.main(verbosity=2)