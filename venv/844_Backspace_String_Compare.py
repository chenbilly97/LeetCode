class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        lenS = len(S)
        lenT = len(T)
        listS = []
        listT = []
        for i in range(lenS):
            if (S[i] == '#'):
                if (len(listS) > 0):
                    del listS[-1]
            else:
                listS.append(S[i])

        for i in range(lenT):
            if (T[i] == '#'):
                if (len(listT) > 0):
                    del listT[-1]
            else:
                listT.append(T[i])

        lenS = len(listS)
        lenT = len(listT)
        if (lenS != lenT):
            return False;
        for i in range(lenS):
            if (listS[i] != listT[i]):
                return False;

        return True;


