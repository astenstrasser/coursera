class ListOfStrings:

    def __init__(self, strings_list):
        self.data = strings_list
        self.sentence = " ".join(strings_list)

    def find_smaller_name(self):
        smaller = " ".join(self.data)
        for string in self.data:
            string = string.strip()
            if len(string) < len(smaller):
                smaller = string.capitalize()
        return smaller

    def order_first_string(self):
        first = 'zzzzz'
        for string in self.data:
            if string.lower() < first.lower():
                first = string
        return first

    def upper_letters(self):
        upper_letters = '' 
        sentence = self.sentence
        sentence = sentence.replace(' ','')
        size = len(sentence)
        for letter in sentence:
            if ord(letter) >= 65 and ord(letter) <= 90:
                upper_letters += letter
        return upper_letters
