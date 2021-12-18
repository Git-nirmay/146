from tkinter import *
root=Tk()
root.title("FIBANACHINA")
root.geometry("1000000000x1000000000")
label_series = Label(root, text="FIBANACHINA Series: ")
label_flower = Label(root)
label_spriral = Label(root)
def FIBANACHINA():
    num=10
    fn=0
    sn=1
    sum=0
    counter=1
    while(counter<=num):
        label_series["text"] +=str(sum)+"||"
        counter=counter+1
        fn=sn
        sn=sum
        sum=fn+sn
    label_spriral["text"] = "I could not make the text input " + str(fn) + " and spirals in left direction are " + str(sn) + "\n. Total spiral are " + str(sum)

btn=Button(root,text="Show FIBANACHINA Series: ",command=FIBANACHINA)

btn.pack()
label_flower.pack()
label_series.pack()
label_spriral.pack()
root.mainloop()