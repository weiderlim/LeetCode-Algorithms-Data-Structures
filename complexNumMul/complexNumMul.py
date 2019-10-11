# for two complex no's "a + bi" and "c + di", the output is always 
# ac + (ad + bc)i + bd i^2, which simplifies to
# ac - bd + (ad + bc)i

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        coeff_1, coeff_2 = self.find_coefficients(a)
        coeff_3, coeff_4 = self.find_coefficients(b)

        # plug in with the simplified formula above with string formatting
        output_string = "{}+{}i"
        return output_string.format(((coeff_1 * coeff_3)-(coeff_2 * coeff_4)), ((coeff_1 * coeff_4)+(coeff_2 * coeff_3)))

    # make sure call the correct coefficients, particularly if they are negative
    def find_coefficients(self, n="str"):
        com_num = list(n)
        # find everything before the "+" sign and assign as coeff_1
        coeff_1 = int("".join((com_num[:com_num.index("+")])))
        # find everything after the "+" sign and assign as coeff_2
        coeff_2 = int("".join((com_num[com_num.index("+") + 1:-1])))
        return coeff_1, coeff_2

obj = Solution()
param_1 = obj.complexNumberMultiply("1+1i", "1+1i")
print (param_1)
param_2 = obj.complexNumberMultiply("1+-1i", "1+-1i")
print (param_2)

# Runtime: 16 ms, faster than 67.58% of Python online submissions for Complex Number Multiplication.
# Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Complex Number Multiplication.

# example solutions : using split("+") would yield tidier code