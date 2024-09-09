class SDES:
    def perFirst(self, plaintext : str) -> str :
        table = [2, 6, 3, 1, 4, 8, 5, 7]
        p_box = ""
        for i in table:
            p_box += plaintext[i-1]
        return p_box

    def perLast(self, plaintext : str) -> str :
        table = [4, 1, 3, 5, 7, 2, 8, 6]
        p_box = ""
        for i in table:
            p_box += plaintext[i-1]
        return p_box

    def p_expansion_box(self, plaintext : str) -> str :
        table = [4, 1, 2, 3, 2, 3, 4, 1]
        p_box = ""
        for i in table:
            p_box += plaintext[i-1]
        return p_box

    def p_straight_box(self, plaintext : str) -> str :
        table = [2, 4, 3, 1]
        p_box = ""
        for i in table:
            p_box += plaintext[i-1]
        return p_box

    def s_box(self, plaintext : str) -> str :
        s1 = [["01", "00", "11", "10"],
            ["11", "10", "01", "00"],
            ["00", "10", "01", "11"],
            ["11", "01", "11", "10"]]
        
        s2 = [["00", "01", "10", "11"],
            ["10", "00", "01", "11"],
            ["11", "00", "01", "00"],
            ["10", "01", "00", "11"]]
        
        row_s1 = int(plaintext[0] + plaintext[3], 2)
        col_s1 = int(plaintext[1] + plaintext[2], 2)
        row_s2 = int(plaintext[4] + plaintext[7], 2)
        col_s2 = int(plaintext[5] + plaintext[6], 2)
        
        return s1[row_s1][col_s1] + s2[row_s2][col_s2]

    def roundFunction(self, plaintext : str, R1 : str) -> str :
        expanded = self.p_expansion_box(plaintext)
        
        xor = ""
        for i in range(len(expanded)):
            xor += str(int(expanded[i]) ^ int(R1[i]))
        
        sbox = self.s_box(xor)
        
        pstraight = self.p_straight_box(sbox)
        
        return pstraight