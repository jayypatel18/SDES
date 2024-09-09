import s_des as moduless
import key_generation as keyer

s1 = keyer.Keyer()
s3 = moduless.SDES()

class Dec:
    def decrypt(self, ciphertext : str, key : str) -> str :
        # intial permutation
        ciphertext = s3.perFirst(ciphertext)
        
        r1, r2 = s1.generateRoundKey(key)
        
        # round function
        right1 = ciphertext[4:]
        round_right1 = s3.roundFunction(right1, r2)
        left1 = ciphertext[:4]

        # XORing
        newLeft1 = ""
        for i in range(len(left1)):
            newLeft1 += str(int(left1[i]) ^ int(round_right1[i]))
            
        # swapper
        right2 = newLeft1
        round_right2 = s3.roundFunction(right2, r1)
        left2 = right1
        
        # XORing
        newLeft2 = ""
        for i in range(len(left2)):
            newLeft2 += str(int(left2[i]) ^ int(round_right2[i]))
            
        final = newLeft2 + right2
        
        plaintext = s3.perLast(final)
        
        return plaintext