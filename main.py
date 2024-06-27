#import cfg as c
import command as cm
#import command.par as par
import osakana
import tkinter
import tkinter.ttk as ttk
from tkinterdnd2 import *
from tkinter import colorchooser
import matplotlib
import matplotlib.pyplot as plt
import re
#import third
#--------------------------------------------------------------
par=cm.par
#--------------------------------------------------------------
matplotlib.use('TkAgg')
#plt.rc('text', usetex=True)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#--------------------------------------------------------------


#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------

#root = tkinter.Tk()
root = TkinterDnD.Tk()
root.geometry('800x700')
root.title("JIMMU version-0.5")
root.resizable(width=True,height=True)





#--------------------------------------------------------------
datanumber=-1;
#--------------------------------------------------------------
#definition
def dvar():return tkinter.DoubleVar(root)
def svar():return tkinter.StringVar(root)
def ivar():return tkinter.IntVar(root)
def bvar():return tkinter.BooleanVar(root)
def frame(a,b):return tkinter.Frame(a,relief='ridge',bd=b)
def label(word,frame,x,y):
	name=tkinter.Label(frame,text=word)
	name.grid(row=x,column=y,sticky=tkinter.E)
	return name;
def pac(frame):frame.pack(fill='x')

root.update()
WP=re.findall(r'\d+',root.geometry())
#--------------------------------------------------------------
#   create radio frame
radioframe=frame(root,1);
pac(radioframe);


#   create canvas to set scrollbar
#https://blog.teclado.com/tkinter-scrollable-frames/
topframe=frame(root,0)
canvas=tkinter.Canvas(topframe,highlightthickness=0)
canvas.pack(side='left',fill='both',expand=True)
canvas.update()

scrollbar = tkinter.Scrollbar(topframe,orient='vertical',command=canvas.yview)
sframe=ttk.Frame(canvas)
pac(sframe);

topframe.pack(fill='both',expand=True)
scrollbar.pack(side='right',fill='y')

def sframebind(event):
	global canvas
	canvas.configure(scrollregion=canvas.bbox('all'))
sframe.bind('<Configure>',sframebind)
canvas.create_window((0,0), window=sframe,anchor='nw',width=int(WP[0])-20)
canvas.configure(yscrollcommand=scrollbar.set)

#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------

#   make frame
#   root > radioframe + topframe
#   topframe > canvas > sframe >


frame1=frame(sframe,1);frame1.pack(fill='both',expand=True)
Frame=[sframe,frame1]

#--------------------------------------------------------------
#--------------------------------------------------------------



#--------------------------------------------------------------
#   parts creation and banish
parts=[];
def repack():
	global datanumber
	global radio
	dn=datanumber;
	for k in range(dn+1):
		parts[k].mframe.pack_forget();
		parts[k].oframe.pack_forget();
		parts[k].framed2.pack_forget();
		parts[k].frameco.pack_forget();
		parts[k].framed3.pack_forget();
	for k in range(dn+1):
		pac(parts[k].mframe)
		pac(parts[k].oframe)
		if radio.get()==0:pac(parts[k].framed2)
		if radio.get()==1:pac(parts[k].frameco)
		if radio.get()==2:pac(parts[k].framed3)
	
def addpart():
	global datanumber;
	datanumber=datanumber+1
	parts.append(cm.par(Frame,datanumber,radio));
	if datanumber > 1:
		parts[-1].filename.set(parts[-2].filename.get()); #refer file name
	print(datanumber)
	for k in range(datanumber+1):
		parts[k].addB.config(command=addpart)
		parts[k].redB.bind('<ButtonPress>',redpart)#
	repack()

def redpart(event):
	global datanumber
	global parts
	print(datanumber)
	for k in range(datanumber+1):
		min=parts[k].redB.winfo_rooty();
		max=min+parts[k].redB.winfo_height();
		if event.y_root > min and event.y_root < max:
			parts[k].mframe.pack_forget();parts[k].oframe.pack_forget();
			del parts[k];
			break;
	datanumber=datanumber-1;
	if datanumber < 0:parts=[];addpart();
	repack()
	
def addcontour(event):
	parts[0].contouraddB[0].config(command=addcontour);
	print(event.widget);
	

def redcontour(event):
	for k in range(datanumber+1):
		for l in range(parts[k].convN):
			break;



for i in range(10):
	for j in range(10):
		radioframe.columnconfigure(index=i,weight=1);
		radioframe.rowconfigure(index=j,weight=1);

#	make radio button to choose 2D or 3D or contour
radio=ivar();
radio.set(0);#   radio button's initial value is set 0 (2D mode)
radiod2=tkinter.Radiobutton(radioframe,value=0,variable=radio,
							text='2D',command=repack)
radioco=tkinter.Radiobutton(radioframe,value=1,variable=radio,
							text='2D-Contour',command=repack)
radiod3=tkinter.Radiobutton(radioframe,value=2,variable=radio,
							text='3D',command=repack)
radiod2.grid(row=0,column=3,sticky=tkinter.W)
radiod3.grid(row=0,column=2,sticky=tkinter.W)
radioco.grid(row=0,column=1,sticky=tkinter.W)

#	make entry form to give each axis names
xaxisname=svar();xaxisname.set("Xaxis $x$");
yaxisname=svar();yaxisname.set("Yaxis $y$");
zaxisname=svar();zaxisname.set("Zaxis $z$");

xaxisE=tkinter.Entry(radioframe,textvar=xaxisname)
yaxisE=tkinter.Entry(radioframe,textvar=yaxisname)
zaxisE=tkinter.Entry(radioframe,textvar=zaxisname)
xaxisE.grid(row=1,column=0,columnspan=1,sticky=tkinter.W+tkinter.E)
yaxisE.grid(row=1,column=1,columnspan=1,sticky=tkinter.W+tkinter.E)
zaxisE.grid(row=1,column=2,columnspan=1,sticky=tkinter.W+tkinter.E)

#	make checkbutton form to give log button
xlogbool=bvar();xlogbool.set(False);
ylogbool=bvar();ylogbool.set(False);
zlogbool=bvar();zlogbool.set(False);

xlogC=tkinter.Checkbutton(radioframe,variable=xlogbool,text="Log X");
ylogC=tkinter.Checkbutton(radioframe,variable=ylogbool,text="Log Y");
zlogC=tkinter.Checkbutton(radioframe,variable=zlogbool,text="Log Z");
xlogC.grid(row=2,column=0,sticky=tkinter.W);
ylogC.grid(row=2,column=1,sticky=tkinter.W);
zlogC.grid(row=2,column=2,sticky=tkinter.W);

#	make entry form to give max and min values
xmax=dvar();xmax.set(1.);
xmin=dvar();xmin.set(0.);
ymax=dvar();ymax.set(1.);
ymin=dvar();ymin.set(0.);
region_i=ivar();region_i.set(0);


xmaxE=tkinter.Entry(radioframe,textvariable=xmax)
xminE=tkinter.Entry(radioframe,textvariable=xmin)
ymaxE=tkinter.Entry(radioframe,textvariable=ymax)
yminE=tkinter.Entry(radioframe,textvariable=ymin) 


radio_region_auto=tkinter.Radiobutton(radioframe,value=0,variable=region_i,
							text='auto range')
radio_region_custom=tkinter.Radiobutton(radioframe,value=1,variable=region_i,
							text='custom range')

radio_region_auto.grid(row=3,column=0,sticky=tkinter.W)
radio_region_custom.grid(row=3,column=1,sticky=tkinter.W)
xrangeL=label("X range:  ",radioframe,4,0)
xminE.grid(row=4,column=1,columnspan=1,sticky=tkinter.W)
xmaxE.grid(row=4,column=2,columnspan=1,sticky=tkinter.W)
yrangeL=label("Y range:  ",radioframe,5,0)
yminE.grid(row=5,column=1,columnspan=1,sticky=tkinter.W)
ymaxE.grid(row=5,column=2,columnspan=1,sticky=tkinter.W)



generalinfo=[xaxisname,yaxisname,zaxisname,
			xlogbool,ylogbool,zlogbool];

#   initial run
addpart();
repack();

#   PLOT AND UPDATE
def plotupdate():
	x=[root,datanumber,parts,generalinfo]
	print(parts[0].filename.get())
	if radio.get()==0:#2D
		print("2D MODE")
		osakana.graphupdatet(x);
	elif radio.get()==1:#2D contur
		print("2D-CONTOUR MODE")
		osakana.graphupdatethc(x);
	elif radio.get()==2:#3D
		print("3D MODE")
		osakana.graphupdateth(x);
update=tkinter.Button(radioframe,text="plot and update!!",command=plotupdate);
update.grid(row=0,column=0,columnspan=1,sticky=tkinter.W+tkinter.E)




root.mainloop()
