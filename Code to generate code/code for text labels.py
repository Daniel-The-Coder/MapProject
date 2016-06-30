y=0.02
for i in range(1,31):
	print("label"+str(i)+' = Label(root, text="'+str(i)+'                                 ")')
	print("label"+str(i)+".config(font=('helvetica',10))")
	print("label"+str(i)+".place(relx=0.77, rely="+str(y+(0.03*(i-1)))+")")
	print()
