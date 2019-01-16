# Class which implements a prefix trie
class Trie:

    # Class which represents a node in a trie
    class Node:
        def __init__(self, character):
            self.character = character
            self.connected_nodes = {}

        def add_connected_node(self, node):
            self.connected_nodes[node.character] = node

    # Class used to create a search in a prefix trie
    class Search:
    
        def __init__(self, start_node, word):
            self.results = []
            self.start_node = start_node
            self.word = word
        
        def search(self, current_node=None, word=None):
            
            if current_node is None:
                current_node = self.start_node
            if word is None:
                word = self.word

            if current_node.connected_nodes:
                for character, node in current_node.connected_nodes.items():
                    if character == '':
                        self.results.append(word)
                    else:
                        self.search(current_node=node, word=word + character)

    # Create a trie with the words in word_dict
    def __init__(self, word_dict):
        self.word_dict = word_dict
        self.root = self.Node('')
        for word in word_dict:
            self.add_word(word, self.root)
        self.words = []

    # Adds the word starting from the current_node
    def add_word(self, word, current_node):
        if word == '':
            current_node.add_connected_node(self.Node(''))
        else:
            letter = word[0]
            word = word[1::]
            found_node = None
            for character, node in current_node.connected_nodes.items():
                if letter == character:
                    found_node = node
                    break
            if found_node is not None:
                self.add_word(word, found_node)
            else:
                new_node = self.Node(letter)
                current_node.add_connected_node(new_node)
                self.add_word(word, new_node) 

    # Finds the node containing the last letter from the word 
    # (this is a recursive function) and uses the 
    # Search class to find all possible words down that node.
    def find_words(self, word, current_node=None, found_words=[], word_trim=''):
        if word == '':
            search = self.Search(current_node, word_trim)
            search.search()
            return search.results
        if current_node is None:
            current_node = self.root
        letter = word[0]
        word = word[1::]
        found_node = None
        for key, value in current_node.connected_nodes.items():
            if letter == key:
                found_node = value
                break
        if found_node is None:
            return []
        else:
            return self.find_words(word, current_node=found_node, word_trim=word_trim + letter)
        


if __name__ == "__main__":
    word_dict = ["dog", "deer", "deal", "deactivate"]
    trie = Trie(word_dict)
    
    query_string = input("Type a prefix: ")

    found_words = trie.find_words(query_string)
    print(found_words)