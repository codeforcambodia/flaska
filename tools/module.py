import os

value = raw_input("Enter your Module Name: ");

newpath = r'../modules/'+value 
if not os.path.exists(newpath):
    os.makedirs(newpath)


filename = '__init__' + '.py'
fo = open(os.path.join(newpath, filename), 'w')
fo.write("from flask import Blueprint"+"\n"+
	value+"= Blueprint("+"'"+value+"'"+", __name__)"+"\n"+
	"from . import controller, routes")
fo.close()	

filename = 'controller' + '.py'
fo = open(os.path.join(newpath, filename), 'w')
fo.write("from flask import render_template"+"\n"+
		 "def Sample():"+"\n\t"+"return 'Hello World';"
		 )
fo.close()	

filename = 'routes' + '.py'
fo = open(os.path.join(newpath, filename), 'w')
fo.write("from . import "+value+"\n"+"from controller import *"+"\n"+
		   "@"+value+".route( '/"+value+"')"+"\n"+"def "+"SampleFunction():"+"\n"
		   +"\t"+"return Sample();"
		  	)
fo.close()	
