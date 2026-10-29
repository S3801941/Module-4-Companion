"""
Module 03: Card Data Mining - Extracting Gold from Deck API
TODO: Navigate complex API data structures and extract specific information

Your mission:
1. Create a deck and extract its ID and metadata
2. Draw cards and extract card details (value, suit, code)
3. Create formatted card descriptions
4. Build a card information system!

Hint: Card data has nested structures - each card has value, suit, code, etc.
"""

import requests
import json

def create_deck_and_extract_info():
    """
    TODO: Create deck and extract key information
    
    Steps to complete:
    1. TODO: Create new deck via API
    2. TODO: Extract deck_id, remaining cards, shuffled status
    3. TODO: Create formatted deck information display
    4. TODO: Return deck_id for drawing cards
    
    Hint: Look for 'deck_id', 'remaining', 'shuffled' in the response
    """
    print("🃏 Creating and analyzing a new deck...")
    
    # TODO: API call to create new deck
    
    url = "https://deckofcardsapi.com/api/deck/new/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    # TODO: Extract key information
    deck_id = data['deck_id']
    remaining = data['remaining'] 
    shuffled = data['shuffled']
    
    # TODO: Display formatted deck info
    print("\n📊 DECK INFORMATION")
    print("-" * 40)
    print(f"Deck ID: {deck_id}")
    print(f"Cards Remaining: {remaining}")
    print(f"Shuffled: {shuffled}")
    
    # TODO: Return deck_id for drawing cards
    return deck_id  # Replace with actual deck_id

def draw_and_analyze_cards(deck_id, count=3):
    """
    TODO: Draw cards and extract detailed card information
    
    Steps to complete:
    1. TODO: Draw cards from the deck using deck_id
    2. TODO: Extract individual card details (value, suit, code, image)
    3. TODO: Create formatted card descriptions
    4. TODO: Display cards in an organized way
    
    Hint: Cards are usually in a 'cards' array, each with 'value', 'suit', 'code'
    """
    if not deck_id:
        print("⚠️ Need a valid deck_id to draw cards!")
        return
    
    print(f"\n🎴 Drawing {count} cards from deck {deck_id}...")
    
    # TODO: API call to draw cards
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    
    # TODO: Extract cards array
    cards = data['cards']  # This should be a list of card dictionaries
    
    # TODO: Display each card nicely
    print("\n🃏 YOUR CARDS:")
    print("=" * 50)
    
    # TODO: Loop through cards and extract info
    for i, card in enumerate(cards, 1):
        value = card['value']
        suit = card['suit'] 
        code = card['code']
        
        print(f"Card {i}: {value} of {suit} (Code: {code})")
    
    print("=" * 50)

def card_collection_summary(deck_id, draw_count=5):
    """
    TODO: Create a comprehensive card analysis system
    
    🎮 Try This: Extend your skills by analyzing multiple cards!
    This function is for when you want to challenge yourself further.
    """
    print(f"\n📈 CARD COLLECTION ANALYSIS")
    print("-" * 40)
    
    # TODO: Draw cards

    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={draw_count}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    cards = data['cards']

    print("\n🃏 YOUR CARDS:")
    print("=" * 50)

    numeric_value = 0
    hearts = 0
    diamonds = 0
    spades = 0
    clubs = 0
    face_cards = []

    
    # TODO: Loop through cards and extract info
    for i, card in enumerate(cards, 1):
        value = card['value']
        suit = card['suit'] 
        code = card['code']
        
        print(f"Card {i}: {value} of {suit} (Code: {code})")

    # TODO: Count suits (Hearts, Diamonds, etc.)

        if suit == "HEARTS":
            hearts += 1
        elif suit == "DIAMONDS":
            diamonds += 1
        elif suit == "SPADES":
            spades += 1
        elif suit == "CLUBS":
            clubs += 1

    # TODO: Identify face cards (Jack, Queen, King)

        if value == "ACE" or "KING" or "QUEEN" or "JACK":
            face_cards.append(i)

    # TODO: Calculate total card value (if numeric)
        if isinstance(value, int):
            numeric_value + value

    print("="*50)
    print()
    print("="*50)
    print("Your Card Statistics")
    print("="*50)
    print("-"*50)
    print("Suit Ammounts")
    print("-"*50)
    print(f"Your {draw_count} cards includes:")
    print(f"{hearts} Heart Cards")
    print(f"{diamonds} Diamond Cards")
    print(f"{spades} Spade Cards")
    print(f"{clubs} Club Cards")
    print()
    print("-"*50)
    print("Face Cards")
    print("-"*50)
    for face_card in face_cards:
        print(f"{face_card} is a face card")
    print()
    print("-"*50)
    print("Card Totals")
    print("-"*50)
    print(f"The number cards have a total of {numeric_value}")




def main():
    """
    TODO: Run your card data extraction system
    """
    print("🎨 Card Data Mining Operation!")
    print("=" * 50)
    
    # TODO: Create deck and get info
    deck_id = create_deck_and_extract_info()  # TODO: Get from create_deck_and_extract_info()
    
    # TODO: Draw and analyze cards 
    draw_and_analyze_cards(deck_id, 3)
    
    # TODO: Try the advanced analysis (when ready)
    card_collection_summary(deck_id, 5)
    
    print("\n✨ You're mining API data like a professional!")

if __name__ == "__main__":
    main()