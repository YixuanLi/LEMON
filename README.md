# LEMON
A local algorithm for fast, high-precision overlapping community detection. 

Requirements
------------
* numpy
* scipy
* pulp ([https://pypi.python.org/pypi/PuLP](https://pypi.python.org/pypi/PuLP))

(may have to be independently installed) 


Usage
-----

######Example Usage######

    $python LEMON.py -f ../example/amazon/graph -g  ../example/amazon/community --sd ../example/amazon/seed --out output.txt

######Command Options######

**-d**: delimiter of input graph and community files [*default: space*]

**-f**:  input network file [*default*: ``example_graphs/amazon/graph``]

  The format of a graph is edgelist, e.g::
  
        1 2
        1 3
        1 4
        ...
**-g**:  input ground truth community file [*default*: ``example_graphs/amazon/community``]

    The format of a ground truth community is a space delimited line of node IDs , e.g:
  
        1 4 8 14 20 21 22                         # community 1
        2 5 3 6 7 15 16 17 18 19                  # community 2
        9 10 11 12 13 23                          # community 3

**--sd**: initial seed set input file [*default*:``example_graphs/amazon/seed``]

    The format of seed set is a single line of space delimited node IDs, e.g:
    
        2 5

**--out**: output file path [*default*: ``output.txt``]

    The output includes the detected community and the similarity between the detected community and ground truth community 
    (quantified by F1 score), e.g:

        # detected community:
        [2,5,3,6,7,15,16,17,18,19]
        # F1 score: 1.0

**-c**: minimum community size [*default*: 20]

**-C**: maximum community size [*default*: 100]

**-e**: expand step [*default*: 6]


######To View Full Command List######

The full list of command line options is available with ``$python LEMON.py --help``

