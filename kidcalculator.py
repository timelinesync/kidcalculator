import webapp2
import cgi

#class calc:
def _float_approx_equal(x, y, tol=1e-18, rel=1e-7):
    if tol is rel is None:
        raise TypeError('cannot specify both absolute and relative errors are None')
    tests = []
    if tol is not None: tests.append(tol)
    if rel is not None: tests.append(rel*abs(x))
    assert tests
    return abs(x - y) <= max(tests)

def add(additionlist, problemsum):
    calculatedsum = 0
    for adden in additionlist:
        calculatedsum += float(adden)
        if _float_approx_equal(float(calculatedsum), float(problemsum)):
            response = problemsum + " is the correct SUM, Great Job!" 
        else:
            response = problemsum + " is not the correct SUM"
    return response

def sub(difference,minuend,subtrahend):
    calculateddifference = float(minuend) - float(subtrahend)
    if _float_approx_equal(float(calculateddifference), float(difference)):
        response = difference + " is the correct DIFFERENCE, Great Job!"
    else:
        response = difference + " is not the correct DIFFERENCE"           
    return response
             
def mul(factorlist,problemproduct):
    calculatedproduct = 1
    for factor in factorlist:
        calculatedproduct *= float(factor)
        if _float_approx_equal(float(calculatedproduct), float(problemproduct)):
            response = problemproduct + " is the correct PRODUCT, Great Job!"
        else:
            response = problemproduct + " is not the correct PRODUCT" 
    return response
def div(quotient,dividend,divisor,remainder):
    calculatedquotient = int(float(dividend) / float(divisor))
    if _float_approx_equal(float(calculatedquotient),float(quotient)) and _float_approx_equal(float(remainder), int(float(dividend) % float(divisor))):
        response = quotient + " r " + remainder + " is the correct QUOTIENT, Great Job!"
    else:
        response = quotient + " r " + remainder + " is not the correct QUOTIENT"                
    return response

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #result = 1 #sub("45","90","45")
        self.response.out.write("""
          
          <html>
            <head>
            </head>
            <body>
            	<h1>Check Addition</h1>
            	<form action="/results" method="post">
            		SUM: <input type="textfield" name=txtSum><br><br>
            		
            		ADDEN: <input type="textfield" name=txtAdden1 value=0><br>
            		ADDEN: <input type="textfield" name=txtAdden2 value=0><br>
            		ADDEN: <input type="textfield" name=txtAdden3 value=0><br>
            		ADDEN: <input type="textfield" name=txtAdden4 value=0><br><br>

            		<input type="submit" value = "Check Addition" name="btnAddition">
            	</form> 
            	<hr>
            	<h1>Check Subtraction</h1>
            	<form action="/results" method="post">

            		DIFFERENCE: <input type="textfield" name=txtDifference><br><br>
            		MINUEND: <input type="textfield" name=txtMinuend><br>
            		SUBTRAHEND: <input type="textfield" name=txtSubtrahend><br><br>
            		<input type="submit" value = "Check Subtraction" name=btnSubtraction>
            	</form> 
            	<hr> 
            	<h1>Check Multiplication</h1>
            	<form action="/results" method="post">

            		PRODUCT: <input type="textfield" name=txtProduct><br><br>
            		FACTOR: <input type="textfield" name=txtFactor1><br>
            		FACTOR: <input type="textfield" name=txtFactor2><br><br>
            		<input type="submit" value = "Check Multiplication" name=btnMultiplication>
            	</form> 
            	<hr>
            	<h1>Check Division</h1>
            	<form action="/results" method="post">

            		QUOTIENT: <input type="textfield" name=txtQuotient><br>
            		REMAINDER: <input type="textfield" name=txtRemainder value="0"><br><br>
            		DIVIDEND: <input type="textfield" name=txtDividend><br>
            		DIVISOR: <input type="textfield" name=txtDivisor><br><br>
            		<input type="submit" value = "Check Division" name=btnDivision>
            	</form> 
            </body>
          </html>

          """)
		
class ResultsPage(webapp2.RequestHandler):
    def post(self):


        #self.response.write('<html><body>You wrote:<pre>')
        #self.response.write(cgi.escape(self.request.get('txtDifference'))) 
        additionlist = []
        problemsum = self.request.get('txtSum')
        additionlist.append(self.request.get('txtAdden1'))
        additionlist.append(self.request.get('txtAdden2'))
        additionlist.append(self.request.get('txtAdden3'))
        additionlist.append(self.request.get('txtAdden4'))

        difference = self.request.get('txtDifference')
        minuend = self.request.get('txtMinuend')
        subtrahend = self.request.get('txtSubtrahend')
        
        factorlist = []
        product = self.request.get('txtProduct')
        factorlist.append(self.request.get('txtFactor1'))
        factorlist.append(self.request.get('txtFactor2'))

        quotient = self.request.get('txtQuotient')
        dividend = self.request.get('txtDividend')
        divisor = self.request.get('txtDivisor')
        remainder = self.request.get('txtRemainder')

        addbutton = self.request.get("btnAddition")
        subbutton = self.request.get("btnSubtraction")
        mulbutton = self.request.get("btnMultiplication")
        divbutton = self.request.get("btnDivision")

        if (len(addbutton) > 0 and len(problemsum) > 0):
                for adden in additionlist:
                    self.response.write(adden + "<br>")
                self.response.write("_____<br><br>")
         	self.response.write(add(additionlist,problemsum))
        elif (len(subbutton) > 0 and len(difference) > 0):
                self.response.write(minuend + "<br>")
                self.response.write(subtrahend + "<br>")
                self.response.write("_____<br><br>")
        	self.response.write(sub(difference,minuend,subtrahend))
        elif (len(mulbutton) > 0 and len(product) > 0):
                for factor in factorlist:
                    self.response.write(factor + "<br>")
                self.response.write("_____<br><br>")
         	self.response.write(mul(factorlist,product))
        elif (len(divbutton) > 0 and len(quotient) > 0):
                self.response.write(dividend + " / " + divisor +"<br>")
                self.response.write("_____<br><br>")
          	self.response.write(div(quotient,dividend,divisor,remainder))
		
	self.response.write("<br><br><a href='/'>Return to Home Page</a>")

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/results', ResultsPage)
], debug=True)
