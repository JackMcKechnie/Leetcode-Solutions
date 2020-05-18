class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_to_domains = {}
        for cpdomain in cpdomains:
            count_paired = cpdomain.split(" ")
            domains = count_paired[1].split(".")
            i = 0
            while i < len(domains):
                domain_str = ".".join(domains[i:len(domains)])
                if domain_str in count_to_domains:
                    count_to_domains[domain_str] = str(int(count_paired[0]) + int(count_to_domains[domain_str]))
                else:
                    count_to_domains[domain_str] = count_paired[0]
                i += 1

        out = []

        for key in count_to_domains:
            out_str = count_to_domains[key] + " " + key
            out.append(out_str)

        return out
