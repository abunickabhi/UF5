"""
Created on Mon Nov 23 10:09:00 2020
@author: abhi
"""
import pandas as pd
import re
#%%
inputdata = quadstxt
for i in (0,len(inputdata)-1):
    inputdata[i] = inputdata[i].lstrip()
    inputdata[i] = inputdata[i].rstrip()

#%%
data = []
new_words_list = [word[::-1] for word in inputdata]
for i in inputdata:
    if len(i) > 1 and i in new_words_list:
        data.append(i)
        
#%% getting the final set of LQs that are unique and need to be added to UF5 list
res = list(set(inputdata)^set(data))
result=[]
for i in res:
    result.append(i[::-1]) #result object contains the final new inverted LQs
    
#%% remove instances 
results = []
for i in range(len(result)):
    if (re.search('h', result[i]) == None and re.search('ae', result[i]) == None and re.search('bf', result[i]) == None and re.search('fb', result[i]) == None
        and re.search('cg', result[i]) == None and re.search('gc', result[i]) == None and re.search('ij', result[i]) == None
        and re.search('ji', result[i]) == None and re.search('lk', result[i]) == None and re.search('kl', result[i]) == None
        and re.search('ea', result[i]) == None and re.search('mn', result[i]) == None and re.search('nm', result[i]) == None
        and re.search('op', result[i]) == None and re.search('po', result[i]) == None and re.search('tq', result[i]) == None
        and re.search('qt', result[i]) == None and re.search('ur', result[i]) == None and re.search('ru', result[i]) == None
        and re.search('sv', result[i]) == None and re.search('vs', result[i]) == None and re.search('dh', result[i]) == None
        ):
        results.append(result[i])
        
#%% remove instances anywhere
# result2 = []
# for i in range(len(result)):
#     if (re.search('h', result[i]) == None 
#         and re.search('a.*e|e.*a', results[i]) == None 
#         and re.search('b.*f|f.*b', results[i]) == None 
#         and re.search('c.*g|g.*c', results[i]) == None  
#         and re.search('i.*j|j.*i', results[i]) == None
#         and re.search('l.*k|k.*l', results[i]) == None 
#         and re.search('m.*n|n.*m', results[i]) == None 
#         and re.search('o.*p|p.*o', results[i]) == None 
#         and re.search('t.*q|q.*t', results[i]) == None
#         and re.search('u.*r|r.*u', results[i]) == None 
#         and re.search('s.*v|v.*s', results[i]) == None 
#         and re.search('d.*h|h.*d', results[i]) == None
#         and re.search('d.*x|x.*d', results[i]) == None
#         ):
#         result2.append(results[i])
        
#%% remove instances anywhere with spaces
result3 = []
for i in range(len(result)):
    if (re.search('h', result[i]) == None 
        and re.search('^a.*e|e.*a*$', results[i]) == None 
        and re.search('^b.*f|f.*b*$', results[i]) == None 
        and re.search('^c.*g|g.*c*$', results[i]) == None  
        and re.search('^i.*j|j.*i*$', results[i]) == None
        and re.search('^l.*k|k.*l*$', results[i]) == None 
        and re.search('^m.*n|n.*m*$', results[i]) == None 
        and re.search('^o.*p|p.*o*$', results[i]) == None 
        and re.search('^t.*q|q.*t*$', results[i]) == None
        and re.search('^u.*r|r.*u*$', results[i]) == None 
        and re.search('^s.*v|v.*s*$', results[i]) == None 
        and re.search('^d.*h|h.*d*$', results[i]) == None
        and re.search('^d.*x|x.*d*$', results[i]) == None
        ):
        result3.append(results[i])


#%%
df = pd.DataFrame(results) 
df.to_excel('D:/Others/Cubing/output.xlsx', sheet_name='sheet1',index=False)