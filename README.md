# LEMON
A local algorithm for fast, high-precision overlapping community detection. 

Usage
-----

######Example Usage######

``$python LEMON.py --out output.txt``



**-f**:  input network file [*default*: ``example_graphs/amazon/graph``]

    The format of a graph is edgelist, e.g::
  
        1 2
        1 3
        1 4
        ...
**-g**:  input ground truth community file [*default*: ``example_graphs/amazon/community``]

    The format of a ground truth community is a space delimited line of node IDs, e.g:
  
        1 4 8                      # community 1
        2 5 3 6 7                  # community 2
        9 10 11 12 13              # community 3
**-d**: delimiter of input graph and community files [*default: space*]

**--out**: output file path [*default*: ``output.txt``]

    The output includes the detected community and the similarity between the detected community and ground truth community 
    (quantified by F1 score), e.g:

        # detected community:
        [2,5,3,6,7]
        # F1 score: 1.0
  
    
Requirements
------------
* numpy
* scipy
* pulp ([https://pypi.python.org/pypi/PuLP](https://pypi.python.org/pypi/PuLP))

(may have to be independently installed) 
