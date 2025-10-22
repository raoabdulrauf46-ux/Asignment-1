
monuments = {
"islamabad" : "Faisal mosque",
"lahore" :  "Minar e pakistan",
"multan" : "mizar of shams tabraiz",
"faisalabad" : "Ghanta ghar",
"karachi" : "Quaid e azam mazar",
"kasur" : "Baba bulla shah mazar",
"Peshawar" : "Bala hisar fort"
}
n = input ("enter any city :").lower()

if n in monuments :
    print (f"the famous monument in this city is {monuments[n]} ")
else :
    print ("Information is not available about this city")