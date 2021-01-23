import pandas as pd

nums=[i+1 for i in range(26)]

upper_case_alphabets=[chr(i) for i in range(65,91)]

data=dict()

for letter in range(26):
	data[upper_case_alphabets[letter]]=nums[letter]

df=pd.DataFrame([nums],index=None,columns=upper_case_alphabets)
df.to_csv('alpha_num.csv')
print(df)
