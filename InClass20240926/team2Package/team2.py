# team2.py

def team2():
 """
 The function is to return a list of dictionaries
 @return dict: list of dictionaries
 """
 student1Attributes = ["Student 1:", {"First Name": "Michael"}, {"Last Name": "Jackson"}, {"Major": "Mechanical Engineering"}, {"Hometown":"Gary, IN"}, {"M Number":"M414351234"}]
 student2Attributes = ["Student 2:", {"First Name": "Elvis"}, {"Last Name": "Presley"}, {"Major": "Primary Education"}, {"Hometown":"Detroit, MI"}, {"M Number":"M123125312"}]
 return student1Attributes, student2Attributes

if __name__ == "__main__":
 print(team2())