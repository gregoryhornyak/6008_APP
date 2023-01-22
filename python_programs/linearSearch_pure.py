def linearSearch(target, inList):
    # base case
    if len(inList) == 0:
        return False
    returnList = ""
    first_element = inList[0]
    rest = inList[1:]
    if first_element != target:
        returnList = rest
        return linearSearch(target,returnList)
    else:
        return True

if __name__ == "__main__":
    print(linearSearch(5,[1,4,8,6]))