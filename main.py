class RunLengthEncoding:
    def __init__(self, string):
        self.string = string

    def encode(self):
        encoded_string = ""
        i = 0

        while i < len(self.string):
            count = 1
            #checks if in bounds and if the current character is the same as the next
            while i + 1 < len(self.string) and self.string[i] == self.string[i+1]:
                i += 1
                count += 1
            if count > 4:
                #if count is greater than 4, add the count and the character to the encoded string
                encoded_string += f"/{count}{self.string[i]}"
            else:
                #if count is less than 4, add the character count times to the encoded string
                encoded_string += self.string[i]*count
            i += 1

        return encoded_string
    
print(RunLengthEncoding("aaabaaaaaaa").encode())
