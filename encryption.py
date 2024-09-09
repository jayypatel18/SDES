import s_des as moduless
import key_generation as keyer

s1 = keyer.Keyer()
s2 = moduless.SDES()

class Enc:
    def encrypt(self, plaintext : str, key : str) -> str :
        # intial permutation
        plaintext = s2.perFirst(plaintext)
        
        r1, r2 = s1.generateRoundKey(key)
        print("\nRound 1 Key: ", r1)
        print("\nRound 2 Key: ", r2)
        
        # round function
        right1 = plaintext[4:]
        round_right1 = s2.roundFunction(right1, r1)
        left1 = plaintext[:4]

        # XORing
        newLeft1 = ""
        for i in range(len(left1)):
            newLeft1 += str(int(left1[i]) ^ int(round_right1[i]))
            
        # swapper
        right2 = newLeft1
        round_right2 = s2.roundFunction(right2, r2)
        left2 = right1
        
        # XORing
        newLeft2 = ""
        for i in range(len(left2)):
            newLeft2 += str(int(left2[i]) ^ int(round_right2[i]))
            
        final = newLeft2 + right2
        
        plaintext = s2.perLast(final)
        
        return plaintext