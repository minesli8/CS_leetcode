class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_converted = []
        
        for email in emails:
            
            sep = email.split('@')
            local_name = sep[0]
            domain = sep[1]
            
            cat = ''
            for char in local_name:
                if char=='.':
                    continue
                if char=='+':
                    break
                cat = cat+char
                
            emails_converted.append(cat+'@'+domain)
            
        return len(set(emails_converted))
