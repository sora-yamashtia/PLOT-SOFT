#import cfg as c
import tkinter
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
from mpl_toolkits.mplot3d import Axes3D


def linestyles():
	lines=[]
	lines=['solid']
	for n in range(5):
		for l in range(5):
			for m in range(5):
				lines.append((0,(2*n+1,3*l+1,2*m+1)))
	return lines
def graphupdatethc(input):#3d contour

	#yet
	logX=False;logY=False;logZ=False;
	sfw=8;sfh=6;
	sml=0.15;smr=0.06;smt=0.06;smb=0.15;
	labelsize=25
	ticsize=15
	# no need datanameco,lgraco,lsselectco,coutourselectco,contournumco

	#general setting
	labelX=input[3][0].get();
	labelY=input[3][1].get();
	labelZ=input[3][2].get();
	logX=input[3][3].get();
	logY=input[3][4].get();
	logZ=input[3][5].get();

	root=input[0];
	datanumber=input[1];
	filename=[];
	datahead=[];
	dataxnum=[];
	dataynum=[];
	colx=[];coly=[];colz=[];
	lw=[];
	for k in range(input[1]+1):
		part=input[2][k];
		filename.append(part.filename.get());
		datahead.append(part.datahead);
		dataxnum.append(part.dataxnum);
		dataynum.append(part.dataynum);
		colx.append(part.colx.get());
		coly.append(part.coly.get());
		colz.append(part.colz.get());
		lw.append(part.linew1.get());
	# only for contour setting
	linec=[];lines=[];clevel=[];
	for k in range(input[1]+1):
		part=input[2][k];
		linec.append([]);
		lines.append([]);
		clevel.append([]);
		for l in range(part.convN):
			linec[k].append(part.linecco[l].get());
			lines[k].append(eval(part.linesco[l].get()));
			clevel[k].append(part.conv[l].get());

	plt.clf();plt.close()

#graph window position
	WP=re.findall(r'\d+',root.geometry())
	GWPx=int(WP[0])+int(WP[2])
	GWPy=int(WP[3])
	gwposition='+'+str(GWPx)+'+'+str(GWPy)
# graph setting
	fig = plt.figure(figsize=(sfw,sfh),
	facecolor="white", edgecolor="coral", linewidth=2) # make figure


	ax3 = plt.axes([sml,smb,1.0-sml-smr,1.0-smt-smb])
	legend=[]
	for k in range(datanumber+1):
		data = np.loadtxt(filename[k],skiprows=datahead[k])
		X=data[:,colx[k]-1]
		Y=data[:,coly[k]-1]
		Z=data[:,colz[k]-1]


############################################################################
#graph1
		X3 = X.reshape(dataxnum[k],dataynum[k])
		x = X3[0:dataxnum[k],1]
		y = Y[0:dataynum[k]]
		x3, y3 = np.meshgrid(x, y)
		z3 = Z.reshape(dataynum[k],dataxnum[k]).T
		 # determine the linestyles 125 pattern
		lws = [0.3,0.3,0.3,0.3,0.3]
		cls = [ [0.0,0.0,0.0],
				[0.0,0.0,0.25],
				[0.0,0.0,0.50],
				[0.0,0.0,0.75],
				[0.0,0.0,1.0]
				]
		cntr = ax3.contour(x3,y3,z3,
				levels = clevel[k],
				linestyles = lines[k],
				linewidths = lw[k],
				colors = linec[k],
				)
		ax3.clabel(cntr,fontsize=15,use_clabeltext=True)#,fmt='%.3e'
	if logX :
		ax3.set_xscale("log")
	if logY:
		ax3.set_yscale("log")
# 目盛方向を両側に設定
# 目盛の長さを5ポイントに設定
# 目盛と目盛ラベルの色をblueに設定
	plt.setp(ax3.get_xticklabels(), fontsize=ticsize)
	plt.setp(ax3.get_yticklabels(), fontsize=ticsize)
	ax3.tick_params(direction = "inout", length = 5, colors = "blue")
	ax3.get_xaxis().set_tick_params(pad=1) #メモリの位置調整
	ax3.minorticks_on() #補助メモリ
	ax3.set_xlabel(labelX, size = labelsize)
	ax3.set_ylabel(labelY, size = labelsize)
	plt.draw()
	plt.pause(0.01)
#plt.draw()
	print(
	re.findall(r'\d+',root.geometry())[0]
	) #root's size and position (0,1,2,3)
	plt.get_current_fig_manager().window.wm_geometry(gwposition)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def graphupdateth(input):#3D

	# not yet
	logX=False;logY=False;logZ=False;
	sfw=8;sfh=6;
	sml=0.1;smr=0.1;smt=0.1;smb=0.1;
	labelsize=25
	ticsize=15

	# general setting
	labelX=input[3][0].get();
	labelY=input[3][1].get();
	labelZ=input[3][2].get();
	logX=input[3][3].get();
	logY=input[3][4].get();
	logZ=input[3][5].get();

	root=input[0];
	datanumber=input[1];
	filename=[];
	datahead=[];
	dataxnum=[];
	dataynum=[];
	colx=[];coly=[];colz=[];
	lw=[];
	lc=[];
	for k in range(input[1]+1):
		part=input[2][k];
		filename.append(part.filename.get());
		datahead.append(part.datahead);
		dataxnum.append(part.dataxnum);
		dataynum.append(part.dataynum);
		colx.append(part.colx.get());
		coly.append(part.coly.get());
		colz.append(part.colz.get());
		lw.append(part.linew1.get());
		lc.append(part.linec1.get());
	# only for 2Dcontour or 3D
	#linec=[];lines=[];clevel=[];

	plotselect=[];
	for k in range(input[1]+1):
		part=input[2][k];
		plotselect.append([]);
		plotselect[k].append(part.plotset[0]);
		plotselect[k].append(part.plotset[1]);
		plotselect[k].append(part.plotset[2]);
	plt.clf()
	plt.close()
#graph window position
	WP=re.findall(r'\d+',root.geometry())
	GWPx=int(WP[0])+int(WP[2])
	GWPy=int(WP[3])
	gwposition='+'+str(GWPx)+'+'+str(GWPy)

# graph setting
	fig = plt.figure(figsize=(sfw,sfh),
	facecolor="white", edgecolor="coral", linewidth=2) # make figure
	ax3 = fig.add_subplot(projection='3d')

	#data = np.loadtxt("res.out",skiprows=1)
	for k in range(datanumber+1):
		data = np.loadtxt(filename[k],skiprows=datahead[k])
		X=data[:,colx[k]-1]
		Y=data[:,coly[k]-1]
		Z=data[:,colz[k]-1]
############################################################################
#graph1
		X3 = X.reshape(dataxnum[k],dataynum[k])
		x = X3[0:dataxnum[k],1]
		y = Y[0:dataynum[k]]
		x3, y3 = np.meshgrid(x, y)
		z3 = Z.reshape(dataynum[k],dataxnum[k]).T

		#	not yet (contour set or not and the value)
		#if contourselect3[k].get()==1:
		#	clevel=getcontour(contourvalue3[k].get())
		#else:
		#	clevel=int(contournum3[k].get())

		cls = [ [0.0,0.0,0.0],
		[0.0,0.0,0.25],
		[0.0,0.0,0.50],
		[0.0,0.0,0.75],
		[0.0,0.0,1.0]
		]
		if logX:x3=np.log(x3)
		if logY:y3=np.log(y3)
		if logZ:z3=np.log(z3)
		#ax3.zaxis._set_scale('log')
		ax3.set_zscale('log')
		ax3.contour(x3,y3,z3,#
				#levels = clevel[k],
				linewidths = 0.6,#float(lw3[k].get()),
				#cmap = lgra3[k].get(), ( not yet )
				offset=z3.min()#offset=-abs(z3).max()
				)
		if plotselect[k][0].get():
			ax3.plot_wireframe(x3,y3,z3,color=lc[k],linewidths=float(lw[k]))
		if plotselect[k][1].get():
			ax3.scatter(x3,y3,z3,color=lc[k],linewidths=float(lw[k]))
		if plotselect[k][2].get():
			ax3.plot_surface(x3,y3,z3,color=lc[k],linewidths=float(lw[k]))


	ax3.set_xlabel(labelX, size = labelsize)
	ax3.set_ylabel(labelY, size = labelsize)
	ax3.set_zlabel(labelZ, size = labelsize)

	plt.setp(ax3.get_xticklabels(), fontsize=ticsize)
	plt.setp(ax3.get_yticklabels(), fontsize=ticsize)
	plt.setp(ax3.get_zticklabels(), fontsize=ticsize)
# 目盛方向を両側に設定
# 目盛の長さを5ポイントに設定
# 目盛と目盛ラベルの色をblueに設定
	ax3.tick_params(direction = "inout", length = 5, colors = "blue")
	ax3.get_xaxis().set_tick_params(pad=1) #メモリの位置調整
	ax3.minorticks_on() #補助メモリ
	plt.draw()
	plt.pause(0.01)
#plt.draw()

	print(
	re.findall(r'\d+',root.geometry())[0]
	) #root's size and position (0,1,2,3)
	plt.get_current_fig_manager().window.wm_geometry(gwposition)



#2D
def graphupdatet(input):
#	(root,datanumber,filename,labelsize,
#	logX,logY,logZ,
#	sfw,sfh,sml,smr,smt,smb,labelX,labelY,labelZ,
#	datahead,dataxnum,dataynum,colx,coly,colz,
#	dataname2,lc2,lw2,ls2a,lsselect2,ls2c)
	# not yet
	logX=False;logY=False;logZ=False;
	sfw=8;sfh=6;
	sml=0.15;smr=0.06;smt=0.06;smb=0.15;
	labelsize=25
	ticsize=15


	# general setting

	labelX=input[3][0].get();
	labelY=input[3][1].get();
	labelZ=input[3][2].get();
	logX=input[3][3].get();
	logY=input[3][4].get();
	logZ=input[3][5].get();

	root=input[0];
	datanumber=input[1];
	filename=[];
	datahead=[];
	dataxnum=[];
	dataynum=[];
	dataname=[];
	colx=[];coly=[];colz=[];
	lw=[];
	lc=[];
	for k in range(input[1]+1):
		part=input[2][k];
		filename.append(part.filename.get());
		datahead.append(part.datahead);
		dataxnum.append(part.dataxnum);
		dataynum.append(part.dataynum);
		colx.append(part.colx.get());
		coly.append(part.coly.get());
		colz.append(part.colz.get());
		lw.append(part.linew1.get());
		lc.append(part.linec1.get());
		dataname.append("not yet");
	# only 2D
	lines=[];#line style
	marks=[];#marker style
	markw=[];# marker size(width)
	for k in range(input[1]+1):
		part=input[2][k];
		lines.append(eval(part.lines1.get()));
		marks.append(part.marks1.get());
		markw.append(part.markw1.get());

	plt.clf()
	plt.close()
#graph window position
	WP=re.findall(r'\d+',root.geometry())
	GWPx=int(WP[0])+int(WP[2])
	GWPy=int(WP[3])
	gwposition='+'+str(GWPx)+'+'+str(GWPy)

# graph setting
	fig = plt.figure(figsize=(sfw,sfh),
	facecolor="white", edgecolor="coral", linewidth=2) # make figure

	ax = plt.axes([sml,smb,1.0-sml-smr,1.0-smt-smb])

	#data = np.loadtxt("res.out",skiprows=1)
	legend=[]
	for k in range(datanumber+1):
		data = np.loadtxt(filename[k],skiprows=datahead[k])
		X=data[:,colx[k]-1]
		Y=data[:,coly[k]-1]

		ax.plot(X,Y,alpha=1.0,
			label="linelabel",
			linestyle=lines[k],
			color=lc[k],
			linewidth=lw[k],
			marker=marks[k],
			markersize=markw[k])
		plt.grid(which="both")
		legend.append(dataname[k])
	if logX:ax.set_xscale("log");
	else:ax.set_xscale("linear");
	if logY:ax.set_yscale("log");
	else:ax.set_yscale("linear");
	ax.legend(legend)
	ax.set_xlabel(labelX, size = labelsize)
	ax.set_ylabel(labelY, size = labelsize)

	plt.setp(ax.get_xticklabels(), fontsize=ticsize)
	plt.setp(ax.get_yticklabels(), fontsize=ticsize)
#	ax.rc('xtick', labelsize=25)
#	plt.rc('ytick', labelsize=25)

	plt.draw()
	plt.pause(0.01)
	print(
	re.findall(r'\d+',root.geometry())[0]
	) #root's size and position (0,1,2,3)
	plt.get_current_fig_manager().window.wm_geometry(gwposition)

#------------------------------------------------------------------------------------------


def Fileanalysis(x):
	name=x[0];
	#print(name);
	file=open(name,'r');
	numline=0;# how many line continues data? (number of y data)
	sline=[];
	datahead=0;
	linenumber=0;
	dataline_start=False;
	for data in file:# data is a string of each line
		linenumber=linenumber+1;
		data=data.rstrip('\n')
		data=data.replace(" ","") #hankaku
		data=data.replace("　","") #zenkaku
		data=data.replace("\t","")
		numbernumber=0;
		for num in range(10):
			#count the number of letters of 0,1,2,..
			numbernumber=numbernumber+data.count(str(num))
		if len(data)-numbernumber < numbernumber:
			# saying 'this line 'data' showing value'
			numline=numline+1;
			dataline_start=True;
		else:
			# saying 'this line 'data' is not showing value'
			if dataline_start:
				sline.append(numline)
			else:
				sline.append(-1)
			numline=0
			#print(numline,sline)
	print("debug debug debug")
	print(numline);
	print(sline);
	datahead=sline.count(-1)
	dataynum=max(sline)
	if sline[-1]!=0:
		dataxnum=sline.count(dataynum)+1
	else:
		dataxnum=sline.count(dataynum)
	file.close()
	x[1]=datahead;
	x[2]=dataxnum;
	x[3]=dataynum;
	#print("data form is ")
	#print(datahead,dataxnum,dataynum)
	return x

def Fileanalysis2(filename):# x is filename
#this function tries to understand the construction of data file 'filename'.
# return value is (first skipped line,number of x-data, number of ydata)
	name=filename;
	#print(name);
	file=open(name,'r');
	numline=0;# how many line continues data? (number of y data)
	sline=[];# show line info
	datahead=0;
	linenumber=0;
	ynum_candidate=[];

	# first data is already read -> True,now on preamble->False
	dataline_start=False;
	for data in file:# data is a string of each line
		linenumber=linenumber+1;
		data=data.rstrip('\n')
		data=data.replace(" ","") #hankaku
		data=data.replace("　","") #zenkaku
		data=data.replace("\t","")
		numbernumber=0;
		for num in range(10):
			#count the number of letters of 0,1,2,..
			numbernumber=numbernumber+data.count(str(num))
		numbernumber=numbernumber+data.count("+");
		numbernumber=numbernumber+data.count("-");
		if len(data)-numbernumber < numbernumber:
			# saying 'this line 'data' showing value'
			numline=numline+1;
			dataline_start=True;
			sline.append(1);
		else:
			# saying 'this line 'data' is not showing value'
			if dataline_start:
				ynum_candidate.append(numline)
			else:
				sline.append(-1)
			numline=0
	print(sline.count(1)/max(ynum_candidate))
	datahead=sline.count(-1)
	dataynum=max(ynum_candidate)
	dataxnum=int(sline.count(1)/max(ynum_candidate))
	file.close()

	y=[filename,datahead,dataxnum,dataynum];
	return y




def getcontour(svar):# e.g. "1.0,2.0,3.0"  --> [1.0,2.0,3.0]
	print(svar.index(","))
	a=""
	result=[]

	if svar.index(",")!=0:
		for l in range(svar.index(",")):
			for k in range(svar.index(",")):
				a=a+svar[0]
				svar=svar[1:]
			svar=svar[1:]
			result.append(float(a))
			a=""
	result.append(float(svar))
	print("result",result)
	return result


def convcomp(x):
	filename=x[0];
	colz=x[1];
	skip=x[2];
	convN=x[3];
	print(filename,skip);
	data=np.loadtxt(filename,skiprows=skip)
	z=data[:,colz-1];
	max=z.max();min=z.min();
	y=[];
	if(min==max):
		for k in range(convN):
			#y.append((min+delta*(k+1))*10**(n+m))
			text="{:.2e}".format(min+0.01*(k-1)*min)
			y.append(text);
		print(y);
		return y;

	delta=(max-min)/(convN+2);
	n=0;m=0;
	if delta < 1.0:
		while delta<1.0:
			delta=delta*10.0;
			n=n-1;
	elif delta > 10.0:
		while delta > 10.0:
			delta=delta/10.0;
			m=m+1;
	delta=np.fix(delta)
	print(n,m,delta);
	min=np.fix(min*10**(-n-m));
	print(min,delta)
	for k in range(convN):
		#y.append((min+delta*(k+1))*10**(n+m))
		text="{}e{:+}".format(min+delta*(k+1),n+m)
		y.append(text);
	print(y);
	return y;
