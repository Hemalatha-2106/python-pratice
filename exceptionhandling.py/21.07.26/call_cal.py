import simple_cal
import date_today
def t_f():
    try:
        print("*****D O *****")
        print("Today:",date_today.today_date())
        print("Yesterday:",date_today.yesterday())
        print("Tomorrow:",date_today.tomorrow())
        print("\n***C O***")
        a=float(input("Enter the a:"))
        b=float(input("Enter the b:"))
        print(f"{a}+{b}={simple_cal.add(a,b)}")
        print(f"{a}-{b}={simple_cal.sub(a,b)}")
        print(f"{a}*{b}={simple_cal.mul(a,b)}")
        print(f"{a}/{b}={simple_cal.div(a,b)}")
    except ZeroDivisionError:
        print("Exception Caught:Cannot divide by zero")
    except ValueError:
        print("Exception Caught:Please enter valid numbers")
    else :
        print("\nExecution successfully excuted without any errors")
    finally:
     print("Program execution completed")
if __name__=="__main__":
 t_f()
        
   