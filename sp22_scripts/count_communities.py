# removing subsets: note that the elements in each set (list) are in sorted order.
# perhaps sort the list of lists so that the sets are listed in longest to shortest, and then going down the list to add into 
# a superlist list?
# n sets, m possible elements per set -> O(nlogn + )
# use a hashmap with key = node number and value starting at 1, multiplied by primes as we add sets into (superset) list? and store the highest current prime val (go up)

def count_communities(path):
    communities = []
    supersets = []

    # convert text file to a list of int lists (each int list is sorted, contains nodes in community)
    file = open(path, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.replace('[', '').replace(']', '').replace(',', '')
        intlist = list(map(int,line.split()))
        communities.append(intlist)
    communities.sort(key = lambda x: len(x), reverse = True)

    # computes the list of superset communities (removes subsets)
    for candidate in communities:
        add_in = True
        for superset in supersets:
            if isSubset(candidate, superset):
                add_in = False
                break
        if add_in:
            supersets.append(candidate)
    
    print(len(supersets))
    
# given two lists of length n (sorted), computes if one is subset of other in O(n)
def isSubset(candidate, superset):
    cand_i = 0
    sup_i = 0
    while (cand_i < len(candidate) and sup_i < len(superset)):
        # if same, increment both
        if candidate[cand_i] == superset[sup_i]:
            cand_i += 1
            sup_i += 1
        # if candidate is higher, increment superset
        elif candidate[cand_i] > superset[sup_i]:
            sup_i += 1
        # if candidate val is lower, then it is not a subset
        else:
            return True
    
    if cand_i == len(candidate):
        return True
    else:
        return False
    
      


count_communities("./test_1/strong-communities-140")
