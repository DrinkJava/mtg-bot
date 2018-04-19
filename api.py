from mtgsdk import Card

def fetch_by_name(name):
    cards = Card.where(name=name).all()
    cards = [c for c in cards if c.image_url != None]
    if not cards:
        return {"Status": -1,
                "Message": "Sorry, no cards were found. Perhaps there is a typo?",
                "Content": []}
    elif len(cards) > 1:
        return {"Status": 2,
                "Message": "I found more than one card that matched that name. I will display the first",
                "Content": cards[0]}
    else:
        return {"Status": 1,
                "Message": "I found this",
                "Content": cards[0]}
