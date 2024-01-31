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
                encoded_string += f"/{count:02d}{self.string[i]}"
            else:
                #if count is less than 4, add the character count times to the encoded string
                encoded_string += self.string[i]*count
            i += 1

        return encoded_string
    
    
print("\n")
print("Testing RunLengthEncoding...")

rle1 = RunLengthEncoding("aaaaa")
print(rle1.encode())  # Expected: /05a

rle2 = RunLengthEncoding("aaaa")
print(rle2.encode())  # Expected: aaaa

rle3 = RunLengthEncoding("abcabcabcabcabc")
print(rle3.encode())  # Expected: abcabcabcabcabc

rle4 = RunLengthEncoding("if(a){if(b){if(c){if(d){if(e){5 deeeeeeep}}}}}")
print(rle4.encode())  # Expected: if(a){if(b){if(c){if(d){if(e){5 d/07ep/05}}}}}

rle5 = RunLengthEncoding("")
print(rle5.encode())  # Expected: 