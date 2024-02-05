public class RunLengthEncoding {
    private String string;

    public RunLengthEncoding(String string) {
        this.string = string;
    }

    public String encode() {
        StringBuilder encodedString = new StringBuilder();
        int i = 0;

        while (i < string.length()) {
            int count = 1;
            //checks if in bounds and if the current character is the same as the next
            while (i + 1 < string.length() && string.charAt(i) == string.charAt(i+1)) {
                i++;
                count++;
            }
            //if count is greater than 4, add the count and the character to the encoded string
            if (count > 4) {
                
                encodedString.append("/").append(String.format("%02d", count)).append(string.charAt(i));
                
            } else {
                //if count is less than 4, add the character count to the encoded string
                for (int j = 0; j < count; j++) {
                    encodedString.append(string.charAt(i));
                }
            }
            i++;
        }

        return encodedString.toString();
    }

    public static void main(String[] args) {
        System.out.println("\n");
        System.out.println("Testing RunLengthEncoding...");
        
        RunLengthEncoding rle1 = new RunLengthEncoding("aaaaa");
        System.out.println(rle1.encode());  // Should print: /05a
    
        RunLengthEncoding rle2 = new RunLengthEncoding("aaaa");
        System.out.println(rle2.encode());  // Should print: aaaa
    
        RunLengthEncoding rle3 = new RunLengthEncoding("abcabcabcabcabc");
        System.out.println(rle3.encode());  // Should print: abcabcabcabcabc
    
        RunLengthEncoding rle4 = new RunLengthEncoding("if(a){if(b){if(c){if(d){if(e){5 deeeeeeep}}}}}");
        System.out.println(rle4.encode());  // Should print: if(a){if(b){if(c){if(d){if(e){5 d/07ep/05}}}}}
    
        RunLengthEncoding rle5 = new RunLengthEncoding("");
        System.out.println(rle5.encode());  // Should print: 
    }
}