def checkcc(ccnumber, l):
    sum = 0
    revccnumber = ccnumber[::-1]
    for i in range(l):
        if i%2 == 0:
            sum = sum + int(revccnumber[i])
        else:
            if int(revccnumber[i])*2 < 10: 
                sum = sum + (int(revccnumber[i])*2)
            else:
                sum = sum + int((int(revccnumber[i])*2/10))
                sum = sum + (int(revccnumber[i])*2%10)
    if(sum%10==0): #CC is valid
        print("valid")

valid =['22', '23', '24', '25', '26', '27', '28', '29', '30', '35', '36', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '81', '97']
decoded= ['QVXSZUVY\ZYYZ[a', 'QOUW[VT^VY]bZ_', 'SPPVSSYVV\YY_\\]', 'RPQRSTUVWXYZ[\]', r'QTVWRSVUXW[_Z`\b', r'SlQRUPXWVo\Vuv_n_\ajjce'] #]
for x in decoded:
    i=30 #30 intersant
    z=""
    for y in x:
        y = ord(y)-i
        y = chr(y)
        i=i+1
        z=z+y
    print(z)
    checkcc(z, len(z))
        


