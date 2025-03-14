import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re

def show_single_integral_interface():#显示一重积分
    clear_window()
    create_single_integral_interface()

def show_double_integral_interface():#显示二重积分
    clear_window()
    create_double_integral_interface()

def show_initial_interface():#初始化
    clear_window()
    tk.Label(root,text="请选择积分类型：", font=custom_font).grid(row=0,column=0,columnspan=2,padx=10,pady=10)
    single_integral_button=tk.Button(root,text="定积分",command=show_single_integral_interface,font=custom_font)
    single_integral_button.grid(row=1,column=0,padx=10,pady=10)
    double_integral_button=tk.Button(root,text="二重积分",command=show_double_integral_interface,font=custom_font)
    double_integral_button.grid(row=1,column=1,padx=10,pady=10)

def clear_window():#清除
    for widget in root.winfo_children():
        widget.destroy()

def create_single_integral_interface():#一重积分界面
    #创建并放置标签和输入框
    tk.Label(root,text="请输入函数表达式：",font=custom_font).grid(row=0,column=0,sticky='e',padx=10,pady=10)
    global function_entry
    function_entry=tk.Entry(root,font=custom_font)
    function_entry.grid(row=0,column=1,padx=10,pady=10)
    tk.Label(root,text="请输入积分下限 a：",font=custom_font).grid(row=1,column=0,sticky='e',padx=10,pady=10)
    global a_entry
    a_entry=tk.Entry(root,font=custom_font)
    a_entry.grid(row=1,column=1,padx=10,pady=10)
    tk.Label(root,text="请输入积分上限 b：",font=custom_font).grid(row=2,column=0,sticky='e',padx=10,pady=10)
    global b_entry
    b_entry=tk.Entry(root,font=custom_font)
    b_entry.grid(row=2,column=1,padx=10,pady=10)
    tk.Label(root,text="请输入分割数 n：",font=custom_font).grid(row=3,column=0,sticky='e',padx=10,pady=10)
    global n_entry
    n_entry=tk.Entry(root,font=custom_font)
    n_entry.grid(row=3,column=1,padx=10,pady=10)
    #创建并放置结果标签
    global result_label,error1_label,result2_label,error2_label,result3_label
    result_label=tk.Label(root,text="",font=custom_font)
    result_label.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
    error1_label=tk.Label(root,text="",font=custom_font)
    error1_label.grid(row=5,column=0,columnspan=2,padx=10,pady=10)
    result2_label=tk.Label(root,text="",font=custom_font)
    result2_label.grid(row=6,column=0,columnspan=2,padx=10,pady=10)
    error2_label=tk.Label(root,text="",font=custom_font)
    error2_label.grid(row=7,column=0,columnspan=2,padx=10,pady=10)
    result3_label=tk.Label(root,text="",font=custom_font)
    result3_label.grid(row=8,column=0,columnspan=2,padx=10,pady=10)
    #创建并放置计算按钮
    calculate_button = tk.Button(root,text="计算定积分",command=calculate_integral,font=custom_font)
    calculate_button.grid(row=9,column=0,columnspan=2,padx=10,pady=10)
    #添加“使用注意事项”按钮
    instructions_button=tk.Button(root,text="使用注意事项",command=show_instructions,font=custom_font)
    instructions_button.grid(row=10,column=0,columnspan=2,padx=10,pady=10)
    #添加“返回”按钮
    back_button=tk.Button(root,text="返回",command=show_initial_interface,font=custom_font)
    back_button.grid(row=11,column=0,columnspan=2,padx=10,pady=10)

def create_double_integral_interface():#二重积分的界面
    #创建并放置标签和输入框
    tk.Label(root, text="请输入函数表达式：",font=custom_font).grid(row=0,column=0,sticky='e',padx=10,pady=10)
    global function_entry
    function_entry=tk.Entry(root,font=custom_font)
    function_entry.grid(row=0,column=1,padx=10,pady=10)
    tk.Label(root,text="请输入积分下限 a：",font=custom_font).grid(row=1,column=0,sticky='e',padx=10,pady=10)
    global a_entry
    a_entry=tk.Entry(root,font=custom_font)
    a_entry.grid(row=1,column=1,padx=10,pady=10)
    tk.Label(root,text="请输入积分上限 b：",font=custom_font).grid(row=2,column=0,sticky='e',padx=10,pady=10)
    global b_entry
    b_entry=tk.Entry(root,font=custom_font)
    b_entry.grid(row=2,column=1,padx=10,pady=10)
    tk.Label(root,text="请输入积分下限 c：",font=custom_font).grid(row=3,column=0,sticky='e',padx=10,pady=10)
    global c_entry
    c_entry=tk.Entry(root,font=custom_font)
    c_entry.grid(row=3,column=1,padx=10,pady=10)
    tk.Label(root,text="请输入积分上限 d：",font=custom_font).grid(row=4,column=0,sticky='e',padx=10, pady=10)
    global d_entry
    d_entry = tk.Entry(root,font=custom_font)
    d_entry.grid(row=4,column=1,padx=10,pady=10)
    tk.Label(root,text="请输入分割数 n：",font=custom_font).grid(row=5,column=0,sticky='e',padx=10,pady=10)
    global n_entry
    n_entry=tk.Entry(root,font=custom_font)
    n_entry.grid(row=5,column=1,padx=10,pady=10)
    global result_label
    result_label=tk.Label(root,text="",font=custom_font)
    result_label.grid(row=6,column=0,columnspan=2,padx=10,pady=10)
    calculate_double_button=tk.Button(root,text="计算二重积分",command=calculate_double_integral,font=custom_font)
    calculate_double_button.grid(row=7,column=0,columnspan=2,padx=10,pady=10)
    instructions_button=tk.Button(root,text="使用注意事项",command=show_instructions,font=custom_font)
    instructions_button.grid(row=8,column=0,columnspan=2,padx=10,pady=10)
    back_button=tk.Button(root,text="返回",command=show_initial_interface,font=custom_font)
    back_button.grid(row=9,column=0,columnspan=2,padx=10,pady=10)

def calculate_integral():#正确输入函数表达式！
    user_input=function_entry.get()
    try:
        a=a_entry.get()
        b=b_entry.get()
        n=int(n_entry.get())
        #处理a和b中的pi
        a=a.replace('pi', str(np.pi))
        b=b.replace('pi', str(np.pi))
        a=eval(a)
        b=eval(b)       
    except ValueError:
        messagebox.showerror("输入错误","请输入有效的数字")
        return
    #预处理用户输入的函数表达式
    user_input=re.sub(r'(?<=\d)(?=\w)','*',user_input)# 在数字和字母之间添加乘法符号
    user_input=user_input.replace('^','**')# 将^替换为**
    user_input=re.sub(r'\bln\((.*?)\)',r'sp.log(\1)',user_input)# 将ln(x)替换为sp.log(x)
    user_input=re.sub(r'\bsqrt\((.*?)\)',r'sp.sqrt(\1)',user_input)# 将sqrt(x)替换为sp.sqrt(x)
    user_input=re.sub(r'\be\b','E',user_input)#将e替换为E
    user_input=re.sub(r'\bpi\b','np.pi',user_input)#将pi替换为np.pi
    #将用户输入的函数表达式转换为可计算的函数
    x=sp.symbols('x')
    f_sympy=sp.sympify(user_input,locals={'sp':sp})
    f_lambda=sp.lambdify(x, f_sympy,'numpy')
    #检查区间[a, b]内的所有值是否在函数的定义域内
    try:
        #检查区间内是否每个点都有定义
        for i in np.linspace(a, b,num=n):#num=n表示生成n个分割点
            f_lambda(i)#尝试计算函数值
    except (ValueError,ZeroDivisionError) as e:
        messagebox.showerror("定义域错误",f"积分区间内有值不在函数的定义域内:{e}")
        return
    try:
        result=Trapezoidal_formula_Method1(f_lambda,a,b,n)  
        result2=Gauss_Legendre_formula_Method2(f_lambda,a,b,n)
        result3=Sympy_formula_Method3(user_input, a, b)
        if result3==sp.oo or result3==-sp.oo:
            raise ValueError("Sympy积分结果为无穷大")
        error1=abs(result-result3)/abs(result3)*100
        error2=abs(result2-result3)/abs(result3)*100
    except ZeroDivisionError as e:
        messagebox.showerror("计算错误",f"计算过程中出现除零错误:{e}")
        return
    except ValueError as e:
        messagebox.showerror("计算错误",str(e))
        return
    result_label.config(text=f"机械求积法结果为:{result}")
    error1_label.config(text=f"相对于Sympy积分的误差:{error1:.5f}%")
    result2_label.config(text=f"高斯-勒让德求积法结果为:{result2}")
    error2_label.config(text=f"相对于Sympy积分的误差:{error2:.5f}%")
    result3_label.config(text=f"Sympy积分结果为:{result3}")

    plot_function(f_lambda, a, b)

def calculate_double_integral():#正确输入二重积分的函数表达式！
    user_input=function_entry.get()
    try:
        a=a_entry.get()
        b=b_entry.get()
        c=c_entry.get()
        d=d_entry.get()
        n=int(n_entry.get())
        #处理a,b,c和d中的pi
        a=a.replace('pi',str(np.pi))
        b=b.replace('pi',str(np.pi))
        c=c.replace('pi',str(np.pi))
        d=d.replace('pi',str(np.pi))
        a=eval(a)
        b=eval(b)
        c=eval(c)
        d=eval(d)
    except ValueError:
        messagebox.showerror("输入错误","请输入有效的数字")
        return
    user_input=re.sub(r'(?<=\d)(?=\w)','*',user_input)
    user_input=user_input.replace('^','**')
    user_input=re.sub(r'\bln\((.*?)\)',r'sp.log(\1)',user_input)
    user_input=re.sub(r'\bsqrt\((.*?)\)',r'sp.sqrt(\1)',user_input)
    user_input=re.sub(r'\be\b','E',user_input)
    user_input=re.sub(r'\bpi\b','np.pi',user_input)
    x, y=sp.symbols('x y')
    f_sympy=sp.sympify(user_input,locals={'sp': sp})
    f_lambda=sp.lambdify((x, y), f_sympy,'numpy')
    f_lambda=np.vectorize(f_lambda)#将f_lambda变为接受数组输入的函数
    try:
        for i in np.linspace(a,b,num=n):
            for j in np.linspace(c,d,num=n):
                f_lambda(i,j)
    except (ValueError, ZeroDivisionError) as e:
        messagebox.showerror("定义域错误",f"积分区间内有值不在函数的定义域内:{e}")
        return
    try:
        result=Sympy_double_integral_Method(user_input,a,b,c,d)
        if result==sp.oo or result==-sp.oo:
            raise ValueError("Sympy积分结果为无穷大")
    except ZeroDivisionError as e:
        messagebox.showerror("计算错误",f"计算过程中出现除零错误:{e}")
        return
    except ValueError as e:
        messagebox.showerror("计算错误",str(e))
        return
    result_label.config(text=f"Sympy二重积分结果为:{result}")
    plot_double_function(f_lambda, a, b, c, d)

def Trapezoidal_formula_Method1(f,a,b,n):#机械求积法求积分
    h=(b-a)/n
    result=0.5*(f(a)+f(b))
    for i in range(1,n):
        result+=f(a+i*h)
    result*=h
    return result

def Gauss_Legendre_formula_Method2(f,a,b,n):#高斯-勒让德求积法求积分
    [x,w]=np.polynomial.legendre.leggauss(n)
    t=0.5*(x+1)*(b-a)+a
    return 0.5*(b-a)*np.sum(w*f(t))

def Sympy_formula_Method3(user_input,a,b):#Sympy求积分
    x=sp.symbols('x')
    f_sympy=sp.sympify(user_input,locals={'sp':sp})
    result=sp.integrate(f_sympy,(x, a, b))
    return result.evalf()

def Sympy_double_integral_Method(user_input,a,b,c,d):#Sympy求二重积分
    x, y=sp.symbols('x y')
    f_sympy=sp.sympify(user_input,locals={'sp': sp})
    result=sp.integrate(f_sympy,(x, a, b),(y, c, d))
    return result.evalf()

def show_instructions():#注意事项
    instructions="使用注意事项:\n1.输入有效的数学表达式。\n2.确保区间[a, b]内的值在函数的定义域内。\n3.使用pi表示圆周率。\n4.使用x作为自变量。\n5.在必要处加必要的括号以及乘号，例如x*sin(x)，而不是xsinx。\n6.二重积分时，自变量为x和y。"
    messagebox.showinfo("使用注意事项",instructions)
    
def plot_function(f,a,b):#画图
    fig, ax=plt.subplots()
    x_vals=np.linspace(a,b,400)
    y_vals=f(x_vals)
    ax.clear()#清除之前的图像
    ax.plot(x_vals,y_vals,label='f(x)')
    ax.fill_between(x_vals,y_vals,alpha=0.3)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()
    canvas=FigureCanvasTkAgg(fig,master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0,column=2,rowspan=10,padx=20,pady=20)

def plot_double_function(f,a,b,c,d):#画三维图
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    x_vals=np.linspace(a,b,100)
    y_vals=np.linspace(c,d,100)
    X,Y=np.meshgrid(x_vals,y_vals)
    Z=f(X,Y)
    ax.plot_surface(X,Y,Z,cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    canvas=FigureCanvasTkAgg(fig,master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0,column=2,rowspan=10,padx=20,pady=20)

#创建主窗口
root=tk.Tk()
root.title("积分计算器")
#设置窗口大小
root.geometry("1000x600")
#设置自定义图标
#root.iconbitmap(r'C:\Users\10044\Downloads\001.ico') #替换为你的图标文件路径
#自定义字体
custom_font=tkFont.Font(family="思源宋体 Bold",size=12)
#创建初始选择界面
tk.Label(root,text="请选择积分类型：",font=custom_font).grid(row=0,column=0,columnspan=2,padx=10,pady=10)
single_integral_button=tk.Button(root,text="定积分",command=show_single_integral_interface,font=custom_font)
single_integral_button.grid(row=1,column=0,padx=10,pady=10)
double_integral_button=tk.Button(root,text="二重积分",command=show_double_integral_interface,font=custom_font)
double_integral_button.grid(row=1,column=1,padx=10,pady=10)

root.mainloop()