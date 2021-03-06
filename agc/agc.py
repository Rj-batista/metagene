#!/bin/env python3
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    A copy of the GNU General Public License is available at
#    http://www.gnu.org/licenses/gpl-3.0.html

"""OTU clustering"""

import argparse
import sys
import os
import gzip
import statistics
from collections import Counter
# https://github.com/briney/nwalign3
# ftp://ftp.ncbi.nih.gov/blast/matrices/
import nwalign3 as nw

__author__ = "Your Name"
__copyright__ = "Universite Paris Diderot"
__credits__ = ["Your Name"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Your Name"
__email__ = "your@email.fr"
__status__ = "Developpement"


def isfile(path):
    """Check if path is an existing file.
      :Parameters:
          path: Path to the file
    """
    if not os.path.isfile(path):
        if os.path.isdir(path):
            msg = "{0} is a directory".format(path)
        else:
            msg = "{0} does not exist.".format(path)
        raise argparse.ArgumentTypeError(msg)
    return path


def get_arguments():
    """Retrieves the arguments of the program.
      Returns: An object that contains the arguments
    """
    # Parsing arguments
    parser = argparse.ArgumentParser(description=__doc__, usage=
                                     "{0} -h"
                                     .format(sys.argv[0]))
    parser.add_argument('-i', '-amplicon_file', dest='amplicon_file', type=isfile, required=True, 
                        help="Amplicon is a compressed fasta file (.fasta.gz)")
    parser.add_argument('-s', '-minseqlen', dest='minseqlen', type=int, default = 400,
                        help="Minimum sequence length for dereplication")
    parser.add_argument('-m', '-mincount', dest='mincount', type=int, default = 10,
                        help="Minimum count for dereplication")
    parser.add_argument('-c', '-chunk_size', dest='chunk_size', type=int, default = 100,
                        help="Chunk size for dereplication")
    parser.add_argument('-k', '-kmer_size', dest='kmer_size', type=int, default = 8,
                        help="kmer size for dereplication")
    parser.add_argument('-o', '-output_file', dest='output_file', type=str,
                        default="OTU.fasta", help="Output file")
    return parser.parse_args()

#==============================================================
# Main program
#==============================================================
def read_fasta(amplicon_file, minseqlen): 
    if amplicon_file.endswith(".gz"): 
        with gzip.open(amplicon_file,"rb") as file: 
            for line in file 
                sequence=next(file) 
                if len(sequence)>=minseqlen: 
                    yield(seq) 
    else: 
        with open(amplicon_file, "r") as files: 
            sequence_2="" 
            for lines in files: 
                if not lines.startswith(">"):
                sequence_2=sequence_2=line.strip() 
                else: 
                    if len(seq)>=minseqlen: 
                        yield(seq) 

def dereplication_fulllength(amplicon_file, minseqlen, mincount):  
    dict = {}
    for sequence in read_fasta(amplicon_file, minseqlen):
        if not sequence in dict:
            dict[sequence] = 0
        dict[sequence] += 1
    for seq, compt in dict: 
        if count >= mincount: 
            yield(seq,compt) 


def get_chunks(sequence,chunk_size):
    seq=[] 
    for i in range(0, len(sequence), chunk_size): 
        seq_part=sequence[i:chunk_size+i] 
        if len(seq_part)==chunk_size: 
        seq.append(seq_part) 
    return(seq) 

def cut_kmer(sequence, kmer_size): 
    for seq in range(len(sequence)-kmer_size+1): 
        yield(sequence[seq:seq+kmer_size])  


 

def main():
    """
    Main program function
    """
    # Get arguments
    args = get_arguments()


if __name__ == '__main__':
    main()