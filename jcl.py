import re
f = open("C:/Users/ChiaJuiYang/Desktop/Apply_Check.txt","r")
lines = f.readlines()
f.close()
hold_action_list = []
ptf_applied_list = []

for i,line in enumerate(lines):
    if line.find("SYSMODS APPLIED") != -1:
        ptf_applied_count = int(line[79:133].strip())
    if line.find("TYPE    REASON ID  FMID     SYSMOD   STATUS    ++HOLD DATA") != -1:
        hold_action_list.append(i)
        # print(max(hold_action_list))
    if line.find("TYPE    REASON ID  REPORT      SYSMODS AFFECTED") != -1:
        ptf_applied_list.append(i)
        # print(max(ptf_applied_list))

# print(min(hold_action_list))
# print(max(hold_action_list))
# print(min(ptf_applied_list))
data=open("C:/Users/ChiaJuiYang/Desktop/abc.txt",'w+')
for i in range(min(hold_action_list),min(ptf_applied_list)):
    print(lines[i].strip('\n'),file=data)
data.close()