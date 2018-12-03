
"""currency.py: Calculate for amount from one type of currency to another.

__author__ = "Ye Weiting"
__pkuid__  = "1600017751"
__email__  = "1600017751@pku.edu.cn"
"""
def main():
    def exchange(currency_from, currency_to, amount_from):
        """Returns: amount of currency received in the given exchange.

        In this exchange, the user is changing amount_from money in 
        currency currency_from to the currency currency_to. The value 
        returned represents the amount in currency currency_to.

        The value returned has type float.

        Parameter currency_from: the currency on hand
        Precondition: currency_from is a string for a valid currency code

        Parameter currency_to: the currency to convert to
        Precondition: currency_to is a string for a valid currency code

        Parameter amount_from: amount of currency to convert
        Precondition: amount_from is a float"""
        from urllib.request import urlopen
        doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode('ascii')
        rejstr=jstr.replace('"',"")
        spjstr=rejstr.split()
        getlist=[i for i in spjstr if "." in i or i.isdecimal()]
        if getlist!=["invalid."]:
            amount=float(getlist[-1])
        else:
            amount="Error"
        return amount
    def test1():
        """test for right imput."""
        assert exchange("USD","EUR",2.0)==1.727138
    def test2():
        """test for wrong imput."""
        assert exchange("USD","ABC",2.0)=="Error"
    def testall():
        test1()
        test2()
        print("All tests passed")
    print(exchange("USD","EUR",2.5))
    testall()
if __name__=="__main__":
    main()