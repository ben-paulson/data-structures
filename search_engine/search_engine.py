"""Search engine using HashMap.
Author: Ben Paulson
"""

import os
import math
from hashtables import HashTableSepchain as HashTable, import_stopwords


class SearchEngine:
    """A search engine to search for terms in documents.
    Attributes:
        directory (str): a directory name
        stopwords (HashTable): a hash table containing stopwords
        doc_length (HashTable): a hash table containing the total
                                number of words in each document
        term_freqs (HashTable): a hash table of hash tables for each term. Each
                                hash table contains the frequency of the term in
                                documents (document names are the keys and the
                                frequencies are the values)
    """
    def __init__(self, directory, stopwords):
        self.directory = directory
        self.stopwords = stopwords
        self.doc_length = HashTable()
        self.term_freqs = HashTable()
        self.index_files(directory)


    def read_file(self, infile):
        """A helper function to read a file
        Args:
            infile (str): the path to a file
        Returns:
            list: a list of str read from a file
        """
        with open(infile, 'r') as inf:
            return inf.readlines()


    def parse_words(self, lines):
        """splits strings into words by spaces.
        Converts words to lower cases, and removes newline chars,
        parentheses, brackets such as "[", "]", "{", "}" and punctuations such
        as ",", ".", "?", "!" Excludes stopwords.
        Args:
            lines (list): a list of strings
        Returns:
            list: a list of words
        """
        words = []
        chars_to_remove = ["(", ")", "[", "]", "{", "}",
                           ",", ".", "?", "!", "\n"]
        for line in lines:
            for char in chars_to_remove:
                line = line.replace(char, "")
            line = line.split(' ')
            for word in line:
                if word.lower() not in self.stopwords and len(word) > 0:
                    words.append(word.lower())
        return words


    def count_words(self, file_path_name, words):
        """count words in a file and store the frequency of each
        word in the term_freqs hash table. Keys of term_freqs are words, values
        are HashTables. Keys of inner hashtables are file names, values are
        frequencies of words.
        Args:
            file_path_name (str): the file name
            words (list) : a list of words
        """
        for word in words:
            if word not in self.term_freqs:
                wordtable = HashTable()
                wordtable[file_path_name] = 1
                self.term_freqs[word] = wordtable
            elif file_path_name not in self.term_freqs[word]:
                self.term_freqs[word][file_path_name] = 1
            else:
                self.term_freqs[word][file_path_name] += 1
        self.doc_length[file_path_name] = len(words)


    def index_files(self, directory):
        """index all text files in a given directory
        Args:
            directory (str): the path of a directory
        """
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            # Only process text files
            if os.path.isfile(path) and os.path.splitext(item)[1] == '.txt':
                lines = self.read_file(path)
                words = self.parse_words(lines)
                self.count_words(path, words)


    def get_wf(self, termf):
        """Computes the weighted frequency
        Arguments:
            termf (float): term frequency
        Returns:
            float: The weighted frequency
        """
        if termf > 0:
            weightedf = 1 + math.log(termf)
        return weightedf


    def get_scores(self, terms):
        """Creates a list of scores for each file in corpus.
        The score = weighted frequency / the total word count in the file
        The score is computed for each term and all scores are summed.
        Arguments:
            terms (list): A list of str
        Returns:
            list: a list of tuples, each containing the file_path_name and
                  its relevancy score
        """
        scores = HashTable()
        results = []
        for term in terms:
            if term in self.term_freqs:
                for file in self.term_freqs[term].keys():
                    term_f = self.term_freqs[term][file]
                    weighted_f = self.get_wf(term_f)
                    if file not in scores:
                        scores[file] = weighted_f
                    else:
                        scores[file] += weighted_f
        for file in scores.keys():
            scores[file] /= self.doc_length[file]
            results.append((file, scores[file]))
        return results


    def rank(self, scores):
        """Ranks files in descending order of relevancy
        Arguments:
            scores (list): a list of tuples: (file_path_name, score)
        Returns:
            list: a list of tuples: (file_path_name, score) sorted in
                  descending order of relevancy
        """
        sorted_idx = len(scores) - 1
        for _ in scores:
            largest_idx = 0
            for j in range(sorted_idx + 1):
                if scores[j][1] < scores[largest_idx][1]:
                    largest_idx = j
            temp = scores[largest_idx]
            scores[largest_idx] = scores[sorted_idx]
            scores[sorted_idx] = temp
            sorted_idx -= 1
        return scores


    def search(self, query):
        """Search for the query items in files.
        Arguments:
            query (str): query input: e.g. "Computer Science"
        Returns:
             list: a list of tuples: (file_path_name, score) sorted
                   in descending order or relevancy, excluding files whose
                   relevancy score is 0
        """
        query_terms = query.lower().strip().split(' ')
        duplicate_check = HashTable()
        for term in query_terms:
            if term not in duplicate_check:
                duplicate_check[term] = 1
            else:
                duplicate_check[term] += 1
        return self.rank(self.get_scores(duplicate_check.keys()))



def main():
    """The main entry point. Displays instructions and asks user for a
    directory to search in, then continually requests search queries until
    the user chooses to quit.
    """
    print("================== INSTRUCTIONS ==================")
    print("1. Enter the name of a directory to search in.")
    print("2. Enter a search query, or quit. To search,")
    print("   prepend your search query with 's:'. For example,")
    print("   's:Computer Science'. Type 'q:' to quit.")
    stopwords = import_stopwords("stop_words.txt", HashTable())
    directory = input("\nEnter a search directory: ")
    engine = SearchEngine(directory, stopwords)
    running = True
    while running:
        query = input("\nEnter a command: ").lower()
        if query[:2] == 's:':
            results = engine.search(query[2:])
            for result in results:
                print(f"{result[0]}: {result[1]}")
        elif query == 'q:':
            running = False


if __name__ == '__main__':
    main()
