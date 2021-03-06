from engine.cards.card import Card
from engine.cards.sticker import Sticker

# from card import Card
# from sticker import Sticker

class Display(Card):

    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''
    def __init__(self, print_data:tuple, card_number:int):
        card_id = "print"
        card_type = [True, True, False, False, False, False, 0]
        super(Display,self).__init__(card_id, card_type, card_number)

        (sticker_type,sticker_value) = print_data
        self.print_data = Sticker(sticker_type,sticker_value)
        self.code = ""

    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_normal"
        print_text = {
            "val_type":"text",
            "text":"Print"
        }
        sticker_text = {
            "val_type": "sticker",
            "sticker_name": self.print_data.sticker_type,
            "sticker_value": self.print_data.sticker_value
        }
        self.card_dict["display"] = [print_text, sticker_text]
        self.card_dict["external_dependant"] = {}
        self.card_dict["children"] = []

        return self.card_dict
    
    def generate_code(self, nesting_level = 0):
        self.code = "print("
        if self.print_data.sticker_type == "variable":
            self.code += self.print_data.sticker_value
        else:
            self.code += '"' + self.print_data.sticker_value + '"'
        self.code += ")\n"

        return self.code

if __name__ == "__main__":
    test_card = Display(("text","Hello World!"), 0)
    print("Card: \n", test_card.generate_card())
    print("Code: \n", test_card.generate_code())

    test_card = Display(("variable","count"), 0)
    print("Card: \n", test_card.generate_card())
    print("Code: \n", test_card.generate_code())