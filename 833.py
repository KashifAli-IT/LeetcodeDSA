
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        bucket = [None] * len(S)
        for i in xrange(len(indexes)):
            if all(indexes[i]+k < len(S) and S[indexes[i]+k] == sources[i][k]
                   for k in xrange(len(sources[i]))):
                bucket[indexes[i]] = (len(sources[i]), list(targets[i]))
        result = []
        i = 0
        while i < len(S):
            if bucket[i]:
                result.extend(bucket[i][1])
                i += bucket[i][0]
            else:
                result.append(S[i])
                i += 1
        return "".join(result)
