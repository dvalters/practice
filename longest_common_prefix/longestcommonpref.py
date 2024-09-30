    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        startl = strs[0][0]

        # Case where there are no matches, return ""
        matches = [x for x in strs if x.startswith(startl)]

        if len(matches) <= 1:
            return ""

        prefix = startl
        for x in strs:
            if x[i]
        return prefix
