class UserAccess:
    def __init__(self, rights, min_permission):
        self.rights = rights
        self.min_permission = min_permission

    def access_rights(self):
        res = ""
        for user in self.rights:
            if user >= self.min_permission:
                res += "A"
            else:
                res += "D"
        return res
    
ua = UserAccess([0,1,2,3,4,5],2)
print(ua.access_rights())   
ua = UserAccess([5,3,2,10,0],20)
print(ua.access_rights())   
ua = UserAccess([],20)
print(ua.access_rights())   
ua = UserAccess([34,78,9,52,11,1],49)
print(ua.access_rights())   
