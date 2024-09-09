class Keyer:
    def p_compression_keygen(self ,key : str) -> str:
        table = [6, 3, 7, 4, 8, 5, 10, 9]
        p_box = ""
        for i in table:
            p_box += key[i-1]
        return p_box
            
    def p_straight_keygen(self, key : str) -> str:
        table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        p_box = ""
        for i in table:
            p_box += key[i-1]
        return p_box
            

    def cshftLeft(self, key : str, shift : int) -> str:
        return key[shift:] + key[:shift]


    def generateRoundKey(self, cipherKeyy : str) -> list[str]:
        # initial P-Box
        cipherKey = self.p_straight_keygen(cipherKeyy)
        
        # Circular Left Shift by 1
        Lciphershfted = self.cshftLeft(cipherKey[:5], 1)
        Rciphershfted = self.cshftLeft(cipherKey[5:], 1)  
        
        # P-Compression Box to get R1
        roundkey1 = self.p_compression_keygen(Lciphershfted + Rciphershfted)
        
        # Circular Left Shift by 2
        Lcipher = self.cshftLeft(Lciphershfted, 2)
        Rcipher = self.cshftLeft(Rciphershfted, 2)
        # P-Compression Box to get R2
        roundkey2 = self.p_compression_keygen(Lcipher + Rcipher)
        
        return [roundkey1, roundkey2]

# cipherKey = "1011100110"
# r1, r2 = self.generateRoundKey(cipherKey)
# print("Round 1 Key: ", r1)
# print("Round 2 Key: ", r2)