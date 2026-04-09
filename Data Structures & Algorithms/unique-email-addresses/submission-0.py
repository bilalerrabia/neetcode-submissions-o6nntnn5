class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        filtred: list = []
        for mail in emails:
            local = mail.split("@")[0]
            domain = mail.split("@")[1]
            mail = list(mail)
            local = local.split("+")[0]
            local = local.replace(".", "")
            print(local, "@", domain)
            filtred.append(str(local + "@" + domain))
        return len(set(filtred))