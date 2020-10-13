"""Huffman Tree functions.
Author: Ben Paulson
"""

from huffman import HuffmanNode
from min_pq import MinPQ
from huffman_bit_writer import HuffmanBitWriter
from huffman_bit_reader import HuffmanBitReader


def cnt_freq(filename):
    """Reads a file and counts the frequency of each character in the file.
    Arguments:
        filename (str): Path to .txt file to read
    Returns:
        list: A list of size 256 containing the frequency counts for all
              8-bit characters in the file
    """
    counts = [0] * 256
    #counts[0] = 1 # Null character
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                counts[ord(char)] += 1
    return counts


def create_huff_tree(list_of_freqs):
    """Creates a huffman tree given a list of character frequencies.
    Arguments:
        list_of_freqs (list): List of character frequencies from cnt_freq()
    Returns:
        The root node of the huffman tree created from the list of frequencies
    """
    pq_arr = []
    for char, freq in enumerate(list_of_freqs):
        if freq > 0:
            pq_arr.append(HuffmanNode(chr(char), freq, None, None))
    min_pq = MinPQ(pq_arr)
    while min_pq.size() > 1:
        left = min_pq.del_min()
        right = min_pq.del_min()
        min_char = min(left.char, right.char)
        parent_node = HuffmanNode(min_char, left.freq + right.freq, left, right)
        min_pq.insert(parent_node)
    return min_pq.min()


def create_code_helper(node, code, all_codes):
    """Helper for create_code. Recursively visits each leaf node,
    updating the code at each path it takes.
    Arguments:
        node (HuffmanNode): The current node being visited.
        code (str): The code to associate with the node if it is a leaf node.
        all_codes (list): List to append code to once it reaches a leaf node.
    """
    if node is None:
        return
    if node.left is None and node.right is None:
        all_codes[ord(node.char)] = code
    create_code_helper(node.left, code + '0', all_codes)
    create_code_helper(node.right, code + '1', all_codes)


def create_code(root_node):
    """Creates a huffman code for each leaf node in a huffman tree.
    Arguments:
        root_node (HuffmanNode): The root node of the huffman tree.
    Returns:
        list: A list of string representations of huffman codes
              for each character in the huffman tree.
    """
    print(root_node)
    codes = [''] * 256
    create_code_helper(root_node, '', codes)
    return codes


def create_header(list_of_freqs):
    """Creates a header for the output file of huffman encoded data.
    The header is a string that consists of each character in the input
    along with its frequency.
    Arguments:
        list_of_freqs (list): List of character frequencies from cnd_freq()
    Returns:
        str: The header to go in the output file
    """
    header = ''
    for char, freq in enumerate(list_of_freqs):
        if freq > 0:
            header += f"{char} {freq} "
    return header


def huffman_encode(in_file, out_file):
    """Reads data from in_file and encodes it using huffman coding,
    writing the encoded data to out_file.
    Arguments:
        in_file (str): Path to file to read data from as input
        out_file (str): Path to file where encoded data will be written.
                        This file will also include a header.
    """
    str_writer = HuffmanBitWriter(out_file)
    bit_writer = HuffmanBitWriter(out_file[:len(out_file) - 4] +
                                  '_compressed.txt')
    try:
        freqs = cnt_freq(in_file)
        header = create_header(freqs)
        huff_tree = create_huff_tree(freqs)
        huff_codes = create_code(huff_tree)
        # for i, code in enumerate(huff_codes):
        #     print(chr(i), code)
        #print(huff_codes)
        # Write headers (Only if file is not empty)
        if len(header.split(' ')) > 3:
            str_writer.write_str(header + '\n')
            bit_writer.write_str(header + '\n')
        # Write data (only if there's more than 1 character)
        if len(header.split(' ')) > 5:
            with open(in_file, 'r') as file:
                for line in file:
                    for char in line:
                        code = huff_codes[ord(char)]
                        str_writer.write_str(code)
                        bit_writer.write_code(code)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {in_file} does not exist")
    finally:
        str_writer.close()
        bit_writer.close()
        pass


huffman_encode("TESTINGITOUT.txt", "TESTINGOUT_SOL")


def parse_header(header_string):
    """Parses the header of an encoded file by creating a list of frequencies.
    Arguments:
        header_string (str): The header to parse.
    Returns:
        list: A list of frequencies for each 8-bit character in the file.
    """
    counts = [0] * 256
    header_data = header_string.strip().split(' ')
    for i in range(0, len(header_data), 2):
        counts[int(header_data[i])] = int(header_data[i + 1])
    return counts


def code_exists(list_of_codes, code):
    """Checks if a code exists in the list of codes.
    Arguments:
        list_of_codes (list): List of string representations of huffman codes.
        code (str): The code to check
    Returns:
        str: The string representation of the index where the code is found
             or None, if the code does not exist in the list of all codes.
    """
    for char, cde in enumerate(list_of_codes):
        if cde == code:
            return chr(char)
    return None


def huffman_decode(encoded_file, decode_file):
    """Decodes data from a file encoded with huffman codes.
    Arguments:
        encoded_file (str): Path to the encoded file to be decoded.
        decode_file (str): Path to the file which will contain the decoded data.
    """
    try:
        reader = HuffmanBitReader(encoded_file)
        # Use decode() to convert bytes to string
        header = reader.read_str()
        # If input file is empty, write empty file and return
        header_info = header.decode().split(' ')
        if len(header_info) <= 3:
            with open(decode_file, 'w') as write_file:
                pass
            reader.close()
            return
        # If only single character, write it and close file, and return
        if len(header_info) == 5:
            msg = ''
            for _ in range(int(header_info[3])):
                msg += chr(int(header_info[2]))
            with open(decode_file, 'w') as write_file:
                write_file.write(msg)
            reader.close()
            return
        list_of_freqs = parse_header(header.decode())
        huff_tree = create_huff_tree(list_of_freqs)
        huff_codes = create_code(huff_tree)
        code = ''
        data_str = ''
        # Read bits
        while True:
            if reader.read_bit():
                code += '1'
            else:
                code += '0'
            character = code_exists(huff_codes, code)
            if character is not None:
                if character == '\x00': # Stop when encounter null char
                    break
                data_str += character
                code = ''
        with open(decode_file, 'w') as write_file:
            write_file.write(data_str)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {encoded_file} does not exist.")
    reader.close()
