class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmailSet = set()

        for email in emails:
            localName, domainName = email.split('@')
            localName = localName.split('+')[0]
            localName = localName.replace('.', '')
            uniqueEmailSet.add((localName, domainName))
        return len(uniqueEmailSet)