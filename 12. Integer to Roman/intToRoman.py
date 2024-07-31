class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Initialize an empty string to build the Roman numeral representation
        roman = ''
        
        # Dictionary that maps integer values to their corresponding Roman numeral symbols
        mapping = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        
        # List to hold each digit of the number, extracted by its place value (units, tens, hundreds, etc.)
        units = []
        
        # Extract each digit from the number starting from the unit place
        while num > 9:
            x = num % 10
            units.append(x)
            num = num // 10  # Use integer division to avoid floating point results
        units.append(num)  # Append the last digit (or the only digit if num < 10)
        
        # The total number of digits
        count = len(units)
        
        # Reverse iterate through each digit and convert it to the corresponding Roman numeral
        for i in range(count-1, -1, -1):
            unit = units[i] * 10**i  # Calculate the actual value of the digit (1, 10, 100, etc.)
            
            # Handle conversion for different magnitudes (thousands, hundreds, tens, units)
            if unit >= 1000:
                # Thousands (M)
                num_first_digit = int(str(unit)[0])
                roman += 'M' * num_first_digit
            elif unit >= 100:
                # Hundreds (C, CD, D, CM)
                num_first_digit = int(str(unit)[0])
                if unit in mapping:
                    roman += mapping[unit]
                elif unit == 400:
                    roman += 'CD'
                elif unit == 900:
                    roman += 'CM'
                elif unit > 500:
                    roman += 'D' + ('C' * (num_first_digit - 5))
                else:
                    roman += 'C' * num_first_digit
            elif unit >= 10:
                # Tens (X, XL, L, XC)
                num_first_digit = int(str(unit)[0])
                if unit in mapping:
                    roman += mapping[unit]
                elif unit == 40:
                    roman += 'XL'
                elif unit == 90:
                    roman += 'XC'
                elif unit > 50:
                    roman += 'L' + ('X' * (num_first_digit - 5))
                else:
                    roman += 'X' * num_first_digit
            else:
                # Units (I, IV, V, IX)
                if unit in mapping:
                    roman += mapping[unit]
                elif unit == 4:
                    roman += 'IV'
                elif unit == 9:
                    roman += 'IX'
                elif unit > 5:
                    roman += 'V' + ('I' * (unit - 5))
                else:
                    roman += 'I' * unit

        return roman
