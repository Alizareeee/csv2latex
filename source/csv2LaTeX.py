import os
from params import *
import sys
def line(number,char="-"):
    response=""
    i=0
    while(i<number):
        response+=char
        i+=1
    return response

def signature(frame=41):
    sign=line(frame,char="%")
    sign = sign + "\n"
    sign = sign + "csv2LaTex project\n for more info please visit : https://github.com/sepandhaghighi/csv2latex\n"
    sign=sign+line(frame,"%")
    return sign
    #% "ModernCV" CV and Cover Letter
    #% LaTeX Template
    #% Version 1.1 (9/12/12)

def escape_char(lines_list):
    for i,item_1 in enumerate(lines_list):
        for j,item_2 in enumerate(item_1):
            for char in char_list:  # instead of using for use a list to find and replace
                lines_list[i][j]=item_2.replace(char,"\\"+char)
    return lines_list


def white_space(line_list):
    len_list = []
    for line in line_list:
        if len(len_list)==0:
            len_list.extend(list(map(len,line)))
        else:
            for i,item in enumerate(line):
                if len(line) <= len(len_list):
                    if len(item) > len_list[i]:
                        len_list[i] = len(item)
    return len_list


def header_handler(file,col_num,caption="my-caption",label="my-label"):
    file.write(header["static_1"])
    file.write(header["static_2"])
    file.write(header["caption"]+"{"+caption+"}\n")
    file.write(header["label"]+"{"+label+"}\n")
    file.write(header["align"]+"{"+"c"*col_num+"}\n")

def footer_handler(file):
    file.write(footer+"\n")


def read_csv(file_name):
    csv_file=open(file_name,"r")
    csv_lines=[]
    for line in csv_file:
        splited_line=line.split(",")
        csv_lines.append(splited_line)
    csv_file.close()
    return csv_lines

def create_latex(file_name,dir_folder="LaTeX",empty_space=True):
    print("\nCreate LaTeX table for "+file_name+" . . .")
    latex_file=open(os.path.join(os.getcwd(),dir_folder+"\\")+file_name[:-4]+".tex","w")
    csv_read=read_csv(file_name)
    csv_lines=csv_read  # continue using csv_read without declairing csv_lines

    col_num=len(csv_lines[0])
    header_handler(latex_file,col_num=col_num) # col_num is useless here
    escape_out=escape_char(csv_lines)
    list_len = white_space(escape_out)
    for item in escape_out :
        for i,item_2 in enumerate(item):
            if i<len(item)-1:
                latex_file.write(item_2)
                if empty_space==True:
                    latex_file.write(" " * (list_len[i]-len(item_2)))
                latex_file.write("&")
                if empty_space==True:
                    latex_file.write(" "*list_len[i])
            else:
                latex_file.write(item_2[:-1])
        latex_file.write("\\\\"+"\n")
    footer_handler(latex_file)
    latex_file.close()
    print("Done!")
    print(line(70, "*"))

def make_dir():
    if "LaTeX" not in os.listdir():
        os.mkdir("LaTeX")

if __name__=="__main__":
    print(signature())
    list_of_files=os.listdir()
    csv_files=[]
    make_dir()
    for i in list_of_files:
        if i.find(".csv")!=-1:
            csv_files.append(i)
    if len(csv_files)==0:
        print("There is no csv file in this folder (Please copy your csv files here)")
        sys.exit()
    else:
        for item in csv_files:
            create_latex(item)








