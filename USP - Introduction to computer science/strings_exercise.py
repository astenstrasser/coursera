class ListOfStrings:

    def __init__(self, strings_list):
        self.data = strings_list

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

