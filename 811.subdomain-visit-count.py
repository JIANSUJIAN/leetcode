#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#


# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)

            # Split the domain into fragments
            fragments = domain.split(".")

            # For each possible subdomain, accumulate the count
            for i in range(len(fragments)):
                subdomain = ".".join(fragments[i:])
                if subdomain not in count_map:
                    count_map[subdomain] = 0
                count_map[subdomain] += count

        #  Convert the count map into the desired format
        return [f"{count} {domain}" for domain, count in count_map.items()]


# @lc code=end
