#import cfg as c
import osakana
import tkinter
import tkinter.ttk as ttk
from tkinterdnd2 import *
import matplotlib
import matplotlib.pyplot as plt
from tkinter import colorchooser

#definition
def dvar(root):return tkinter.DoubleVar(root)
def svar(root):return tkinter.StringVar(root)
def ivar(root):return tkinter.IntVar(root)
def bvar(root):return tkinter.BooleanVar(root)
def frame(a,b):return tkinter.Frame(a,relief='ridge',bd=b)
def label(word,frame,x,y):  #make tkinter,Label
	name=tkinter.Label(frame,text=word)
	name.grid(row=x,column=y,sticky=tkinter.E)
	return name;
def pac(frame):frame.pack(fill='x') #make frame.pack()
def color(event,linec,linecB,dn):  # color chooser for linec1
	for k in range(dn):
		ymin=linecB[k].winfo_rooty()
		ymax=ymin+linecB[k].winfo_height()
		xmin=linecB[k].winfo_rootx()
		xmax=xmin+linecB[k].winfo_width()
		if event.y_root>ymin and event.y_root<ymax and event.x_root>xmin and event.x_root<xmax:
			linec[k].set(colorchooser.askcolor()[1])
			linecB[k].config(fg=linec[k].get())





class par:

	def __init__(self,Frame,datanumber,radio):

		root=Frame[0];
		dn=datanumber;
		# line style list
		lslist=['(0,(1,0))','(0,(1,1))','(0,(3,1))','(0,(3,3))',
				'(0,(1,5,2,5))','(0,(1,2,5,2))','(0,(5,2,3,1))',
				'(0,(1,2,3,2))','(0,(3,1,3,2))','(0,(1,2,1,3))']
		# this can be convert to list using 'eval()'


		# dot style list
		dotlist=['None','.',',','o','v','^','<','>','1','2','3','4','8',
				's','p','*','h','H','+','x','D','d','|','_']

		self.oframe=frame(Frame[1],10);   #optionframe***************************************
		self.mframe=frame(Frame[1],1); #mainframe*****************************************
		pac(self.mframe);pac(self.oframe);

		self.framed2=frame(self.oframe,1);
		self.frameco=frame(self.oframe,1);
		self.framed3=frame(self.oframe,1);

		# this needs at self.colz command ==============================
		def ContourValueSet():
			# variables are difined at 2D contour program area.
			conanalysis=[self.filename.get(),self.colz.get(),self.datahead,self.convN]
			conanalysis=osakana.convcomp(conanalysis)
			for k in range(self.convN):
				self.conv[k].set(conanalysis[k])
		#================================================================

		#global among 2d, 3d, 2dcontour
		#   filename and entry
		self.filename=svar(root);
		#self.filename.set(">> drop the data file here <<");
		
		self.filename.set("histogram0.dat");
		self.filename.set(dn);
		self.pathE=tkinter.Entry(self.mframe,textvar=self.filename,width=45)
		#   column x,y,z
		self.colx=ivar(root);self.coly=ivar(root);self.colz=ivar(root);
		self.colx.set(2);self.coly.set(3);self.colz.set(4);
		self.colxS=tkinter.Spinbox(self.mframe,textvar=self.colx,
									from_=1,to=99,increment=1,width=5)
		self.colyS=tkinter.Spinbox(self.mframe,textvar=self.coly,
									from_=1,to=99,increment=1,width=5)
		self.colzS=tkinter.Spinbox(self.mframe,textvar=self.colz,
									from_=1,to=99,increment=1,width=5,
									command=ContourValueSet)
		#   data label
		self.dataname=svar(root);self.dataname.set("Data $Label$");
		self.datanameE=tkinter.Entry(self.mframe,textvar=self.dataname)
		#   add and reduce button
		self.addB=tkinter.Button(self.mframe,text="+")
		self.redB=tkinter.Button(self.mframe,text="-")


		#----------------------------------------------------------------------
		#position set
		self.pathE.grid(row=1,column=0, ipady=20,columnspan=4);
		self.addB.grid(row=1,column=5,
			sticky=tkinter.W+tkinter.E+tkinter.N+tkinter.S);
		self.redB.grid(row=1,column=6,
			sticky=tkinter.W+tkinter.E+tkinter.N+tkinter.S);

		self.datanameE.grid(row=2,column=0);
		self.colxS.grid(row=2,column=1);
		self.colyS.grid(row=2,column=2);
		self.colzS.grid(row=2,column=3);





		#-----------------------------------------------------------------------
		#-----------------------------------------------------------------------
		#SHARE VARIABLE
		#   first line color	2d and 3D
		self.linec1=svar(root);self.linec1.set("#9700ff");
		#   first line width	2d and 3D and co
		self.linew1=dvar(root);self.linew1.set(1.0);
		#   first line style	2d and 3D
		self.lines1=svar(root);self.lines1.set(lslist[0]);
		#   first marker style	 2d and 3D
		self.marks1=svar(root);self.marks1.set("None");
		#   first marker width(size)	  2d and 3D
		self.markw1=dvar(root);self.markw1.set(1.0);
		#-----------------------------------------------------------------------
		#2D
		#   line color, size and style using self.linec1 & self.linew1 & self.lines1
		self.linec1L=label("line color:",self.framed2,0,0);
		self.linec1B=tkinter.Button(self.framed2,textvariable=self.linec1,
			fg=self.linec1.get())
		self.linew1L=label("line width:",self.framed2,1,0);
		self.linew1S=tkinter.Spinbox(self.framed2,textvariable=self.linew1,
			from_=0,to=4.0,increment=0.2)
		self.lines1L=label("line style:",self.framed2,2,0);
		self.lines1S=tkinter.Spinbox(self.framed2,textvariable=self.lines1,
			values=lslist)
		#   dot style and dot size using self.mark1s & self.mark1w
		self.marks1L=label("marker style:",self.framed2,3,0);
		self.marks1S=tkinter.Spinbox(self.framed2,textvariable=self.marks1,
			values=dotlist)
		self.markw1L=label("marker size:",self.framed2,4,0);
		self.markw1S=tkinter.Spinbox(self.framed2,textvariable=self.markw1,
			from_=0,to=10.0,increment=0.5)
		##################################################################
		# grid position set
		self.linec1B.grid(row=0,column=1);
		self.linew1S.grid(row=1,column=1);
		self.lines1S.grid(row=2,column=1);
		self.marks1S.grid(row=3,column=1);
		self.markw1S.grid(row=4,column=1);
		pac(self.framed2)


		##################################################################
		##################################################################
		##################################################################

		#2D contour (5 elements at first)
		#   contour value
		self.conv=[];self.convE=[]
		#   line color
		self.linecco=[];self.lineccoB=[];
		#   line styles
		self.linesco=[];self.linescoS=[];
		#.  add and reduce button of contour value
		self.contouraddB=[];
		self.contourredB=[];

		def addcontour(event):
			self.convN = self.convN+1;
			k=self.convN-1;
			#   contour value
			self.conv.append(dvar(root))
			self.convE.append(tkinter.Entry(self.frameco,textvar=self.conv[k],width=8))
			self.conv[k].set(0.0+k)
			#   line color
			self.linecco.append(svar(root));
			self.linecco[k].set("#9700ff")
			self.lineccoB.append(tkinter.Button(self.frameco,textvariable=self.linecco[k],
			fg=self.linecco[k].get(),width=5))
			#   line style
			self.linesco.append(svar(root));
			self.linescoS.append(tkinter.Spinbox(self.frameco,
				textvariable=self.linesco[k],values=lslist,width=8))
			l=k%10;self.linesco[k].set(lslist[l]);
			#.  add and reduce button of contour value
			self.contouraddB.append(tkinter.Button(self.frameco,text="+"));
			self.contouraddB[k].bind('<ButtonPress>',addcontour)
			self.contourredB.append(tkinter.Button(self.frameco,text="-"))
			self.contourredB[k].bind('<ButtonPress>',redcontour)
			#
			self.frameco.pack_forget();
			for k in range(self.convN):
				self.convE[k].grid(row=k+1,column=0,ipadx=30)
				self.lineccoB[k].grid(row=k+1,column=2,ipadx=0,padx=30)
				self.linescoS[k].grid(row=k+1,column=4,ipadx=10)
				self.contouraddB[k].grid(row=k+1,column=6,padx=20)
				self.contourredB[k].grid(row=k+1,column=8,padx=0)
			pac(self.frameco);

		def redcontour(event):
			for k in range(self.convN):
				if event.widget==self.contourredB[k]:
					print(k);print(event.widget);print(self.contourredB[k]);
					self.convE[k].grid_forget();
					self.lineccoB[k].grid_forget();
					self.linescoS[k].grid_forget();
					self.contouraddB[k].grid_forget();
					self.contourredB[k].grid_forget();
					del self.conv[k],self.convE[k];
					del self.linecco[k],self.lineccoB[k];
					del self.linesco[k],self.linescoS[k];
					del self.contouraddB[k],self.contourredB[k];
					print(self.convN);print(k);
					break;
			self.convN=self.convN-1;
			#   position set
			self.frameco.pack_forget();
			for k in range(self.convN):
				self.convE[k].grid(row=k+1,column=0,ipadx=30)
				self.lineccoB[k].grid(row=k+1,column=2,ipadx=0,padx=30)
				self.linescoS[k].grid(row=k+1,column=4,ipadx=10)
				self.contouraddB[k].grid(row=k+1,column=6,padx=20)
				self.contourredB[k].grid(row=k+1,column=8,padx=0)
			pac(self.frameco);


		#   the number of the contour values
		self.convN=5;##################the number will be set with + and - button of contour
		for k in range(self.convN):
			self.conv.append(dvar(root))#   contour value

		for k in range(self.convN):
			#   contour value
			self.conv.append(dvar(root))
			self.convE.append(tkinter.Entry(self.frameco,textvar=self.conv[k],width=8))
			self.conv[k].set(0.0+k)
			#   line color
			self.linecco.append(svar(root));
			self.linecco[k].set("#9700ff")
			self.lineccoB.append(tkinter.Button(self.frameco,textvariable=self.linecco[k],
				fg=self.linecco[k].get(),width=5))

			#   line style
			self.linesco.append(svar(root));
			self.linescoS.append(tkinter.Spinbox(self.frameco,
							textvariable=self.linesco[k],values=lslist,width=8))
			self.linesco[k].set(lslist[k]);
			#.  add and reduce button of contour value
			self.contouraddB.append(tkinter.Button(self.frameco,text="+"));
			self.contouraddB[k].bind('<ButtonPress>',addcontour)
			self.contourredB.append(tkinter.Button(self.frameco,text="-"))
			self.contourredB[k].bind('<ButtonPress>',redcontour)

		#   position set
		for k in range(self.convN):
			self.convE[k].grid(row=k+1,column=0,ipadx=30)
			self.lineccoB[k].grid(row=k+1,column=2,ipadx=0,padx=30)
			self.linescoS[k].grid(row=k+1,column=4,ipadx=10)
			self.contouraddB[k].grid(row=k+1,column=6,padx=20)
			self.contourredB[k].grid(row=k+1,column=8,padx=0)

		#   Labels
		self.convL=label("Contour Value",self.frameco,0,0);
		self.lineccoL=label("Line Colors",self.frameco,0,2);
		self.linescoL=label("Line Styles",self.frameco,0,4);






		pac(self.frameco)

		##################################################################
		##################################################################
		##################################################################

		#3D
		#   first line color	#variable is shareed
		self.linec3L=label("line color:",self.framed3,0,0);
		self.linec3B=tkinter.Button(self.framed3,textvariable=self.linec1,
			fg=self.linec1.get())
		#   first line width	#variable is shared
		self.linew3L=label("line width:",self.framed3,1,0);
		self.linew3S=tkinter.Spinbox(self.framed3,textvariable=self.linew1,
			from_=0,to=4.0,increment=0.2).grid(row=1,column=1);
		#   plot type
		self.plottL=label("plot type:",self.framed3,2,0);
		self.plotset=[];
		self.plotset.append(bvar(root));self.plotset[0].set(True);
		self.plotset.append(bvar(root));self.plotset[1].set(False);
		self.plotset.append(bvar(root));self.plotset[2].set(False);

		self.plotwire=tkinter.Checkbutton(self.framed3,variable=self.plotset[0],
			text='wire').grid(row=2,column=1)
		self.plotscat=tkinter.Checkbutton(self.framed3,variable=self.plotset[1],
			text='scatter').grid(row=2,column=2)
		self.plotsurf=tkinter.Checkbutton(self.framed3,variable=self.plotset[2],
			text='surface').grid(row=2,column=3)


		#position set
		self.linec3B.grid(row=0,column=1);

		pac(self.framed3)




		#   event set
		#   datafile drag and drop
		self.datahead=1;
		self.dataxnum=0;
		self.dataynum=0;
		def drop(event):
			self.filename.set(event.data)
			if (event.data[0]=='{') and  (event.data[-1]=='}'):
				dammy=list(event.data);
				dammy[0]='';dammy[-1]='';
				dammy="".join(dammy);
				self.filename.set(dammy);
			fanalysis=[self.filename.get(),self.datahead,self.dataxnum,self.dataynum]
			fanalysis=osakana.Fileanalysis2(fanalysis[0]);
			self.datahead=fanalysis[1];
			self.dataxnum=fanalysis[2];
			self.dataynum=fanalysis[3];
			#contour value analysis
			conanalysis=[self.filename.get(),self.colz.get(),self.datahead,self.convN]
			conanalysis=osakana.convcomp(conanalysis)
			for k in range(self.convN):
				self.conv[k].set(conanalysis[k])


		self.pathE.drop_target_register(DND_FILES) #??
		self.pathE.dnd_bind('<<Drop>>', drop)#



		#   color chooser for 1 and 3 dimension
		def color1(event):  # color chooser for linec1
			self.linec1.set(colorchooser.askcolor()[1])
			self.linec1B.config(fg=self.linec1.get())
			self.linec3B.config(fg=self.linec1.get())
		self.linec1B.bind('<ButtonPress>',color1)#
		self.linec3B.bind('<ButtonPress>',color1)#
		#   color chooser for dn dimension
		def colorB(event):
			color(event,self.linecco,self.lineccoB,self.convN)
		for k in range(self.convN):
			self.lineccoB[k].bind('<ButtonPress>',colorB)#

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
