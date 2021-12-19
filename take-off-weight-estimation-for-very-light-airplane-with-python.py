import numpy as np

# for automated WTO guessing
A = -0.1440
B = 1.1162
W_pl = 60
W_crew = 350
W_tfo = 0.005
M_ff = 0.89183
W_tog = float(input("Enter your take off weight guess: "))
W_eAllow = 10 ** (((np.log10(W_tog))-A)/B)
W_fused = W_tog*(1 - M_ff)
W_fres = A*W_fused
W_f = W_fused+W_fres
W_oEtent = W_tog - W_f - W_pl
W_eTent = W_oEtent - (W_tfo*W_tog) - W_crew
x= W_eAllow - W_eTent

if 0.005<=x<0.006:
    print('good guess')
else:      
    while 0.005>x or x>=0.006:
            if x<0:
                A = -0.1440
                B = 1.1162
                W_pl = 60
                W_crew = 350
                W_tfo = 0.00145
                M_ff = 0.89183
                W_tog -= 0.001
                W_eAllow = 10 ** (((np.log10(W_tog))-A)/B)
                W_fused = W_tog*(1 - M_ff)
                W_fres = A*W_fused
                W_f = W_fused+W_fres
                W_oEtent = W_tog - W_f - W_pl
                W_eTent = W_oEtent - (W_tfo*W_tog) - W_crew
                x= W_eAllow - W_eTent
                print(W_tog, x)
                if 0.005<=x<0.006:
                    print(W_tog, x)
            else:
                A = -0.1440
                B = 1.1162
                W_pl = 60
                W_crew = 350
                W_tfo = 0.005
                M_ff = 0.89183
                W_tog += 0.001
                W_eAllow = 10 ** (((np.log10(W_tog))-A)/B)
                W_fused = W_tog*(1 - M_ff)
                W_fres = A*W_fused
                W_f = W_fused+W_fres
                W_oEtent = W_tog - W_f - W_pl
                W_eTent = W_oEtent - (W_tfo*W_tog) - W_crew
                x= W_eAllow - W_eTent
                print(W_tog, x)
                if 0.005<=x<0.006:
                    print(W_tog, x)

# for manual WTO guessing                       
'''
if 0.005<=x<0.006:
    print("W_eAllow - W_eTent is", x, "good guess")
else:
    print("W_eAllow - W_eTent is", x, "enter another guess")
'''