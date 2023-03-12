
def preprocess(tmp: str) -> str:

# tmp = ""
# with open('input.txt', 'r', encoding='utf-8') as file:
#     tmp += file.read()


    s = [''] * len(tmp)
    for i in range(len(tmp)):
        s[i] = tmp[i]

    for i in range(1, len(s) - 1):
        if (s[i - 1] == ' ' and s[i + 1] == ' ' and s[i] == '-'):
            s[i - 1] = '_'
            s[i + 1] = '_'

    for i in range(5, len(s) - 5):
        if (s[i - 5] >= '0' and s[i - 5] <= '9') and (s[i - 4] >= '0' and s[i - 4] <= '9') and (s[i - 3] == ':') and (s[i - 2] >= '0' and s[i - 2] <= '9') and (s[i - 1] >= '0' and s[i - 1] <= '9') and s[i] == ' ':
            if (s[i + 1] >= '0' and s[i + 1] <= '9') and (s[i + 2] >= '0' and s[i + 2] <= '9') and (s[i + 3] == ':') and (s[i + 4] >= '0' and s[i + 4] <= '9') and (s[i + 5] >= '0' and s[i + 5] <= '9'):
                s[i] = '^'

    for i in range(len(s) - 4):
        if (s[i] == ' ') and (s[i + 1] >= '0' and s[i + 1] <= '9') and (s[i + 2] >= '0' and s[i + 2] <= '9') and (s[i + 3] >= '0' and s[i + 3] <= '9') and (s[i + 4] == ' '):
            s[i + 4] = '/'

    for i in range(len(s) - 2):
        if s[i] == "'" and s[i + 1] == ' ' and s[i + 2] == '(':
            s[i + 1] = ','

        if s[i] == '.' and s[i + 1] == ',' and s[i + 2] == ' ':
            s[i + 1] = ';'
        

    res = ""

    i = 0
    while i + 5 <= len(s):
        if s[i] == '2' and s[i + 1] == '1' and s[i + 2] == ':' and s[i + 3] == '0' and s[i + 4] == '0':
            res += s[i]
            res += s[i + 1]
            res += s[i + 2]
            res += s[i + 3]
            res += s[i + 4]
            res += '\n'
            i += 6
        else:
            res += s[i]
            i += 1

    # print(res)

    days = [""] * 6
    i = 0
    k = 0
    d = ""
    while i < len(res):
        if res[i] == '\n':
            days[k] = d
            k += 1
            d = ""
        else:
            d += res[i]
        i += 1


    schedule = {}
        
    for data in days:
        ans = ""
        i = 0
        j = 1
        while j <= len(data):
            if i == len(data) - 1:
                ans += data[i]
                break
            if (((data[i] >= 'А' and data[i] <= 'Я') or (data[i] >= 'а' and data[i] <= 'я')) and (data[j] >= '0' and data[j] <= '9')) or ((data[i] >= '0' and data[i] <= '9') and data[j] == '^') or (data[i] == '*' and data[j] == ' ') or ((data[i] >= '0' and data[i] <= '9') and (data[j] == '/')):
                ans += data[i]
                if data[j] == '/':
                    ans += data[j]
                ans += '\n'
            else:
                if data[i] != '/':
                    ans += data[i]
            i += 1
            j += 1

        ans = ans.replace('^', ' ')
        ans = ans.replace('_', ' ')
        ans += '\n'

        res = ""

        for i in range(len(ans) - 1):
            if (ans[i] >= '0' and ans[i] <= '9') and (ans[i + 1] == '\n'):
                res += ans[i]
                res += "\nУроков нету"
            elif (ans[i] >= '0' and ans[i] <= '9') and ((ans[i + 1] >= 'a' or ans[i + 1] >= 'А') and (ans[i + 1] <= 'я' or ans[i + 1] <= 'Я')):
                res += ans[i]
                res += '\n'
            else:
                res += ans[i]

        res += '\n'

        # print(res)


        weeks = []
        times = []
        subjects = []
        type_of_subjects = []
        teacher_of_subjects = []
        cabinet_of_subjects = []


        i = 0
        step = 0
        while i < len(res):
            p = ""
            while res[i] != '\n':
                p += res[i]
                i += 1
            i += 1
            # print(p)
            step += 1
            if step == 1:
                # print("Day: ", p)
                weeks.append(p)
            else:
                if step % 2 == 0:
                    # print("Times: ", p)
                    times.append(p)
                else:
                    # print("Object: ", p)
                    q = ""
                    l = 0
                    u = 0
                    if p == "Уроков нету":
                        subjects.append("-")
                        type_of_subjects.append("-")
                        teacher_of_subjects.append("-")
                        cabinet_of_subjects.append("-")
                    while l < len(p) and p[l] != '\n':
                        if p[l] == ',':
                            u += 1
                            if u == 1:
                                # print("Subject: ", q)
                                subjects.append(q)
                            elif u == 2:
                                # print("Type of Subject: ", q)
                                type_of_subjects.append(q)
                            elif u == 3:
                                # print("Teacher: ", q)
                                teacher_of_subjects.append(q)
                            elif u == 4:
                                # print("Room: ", q)
                                cabinet_of_subjects.append(q)
                            q = ""   
                        else:
                            q += p[l] 
                        l += 1


        # print(subjects)
        # print(type_of_subjects)
        # print(teacher_of_subjects)
        # print(cabinet_of_subjects)

        for w in weeks:
            schedule[w] = []
            for a, b, c, d, e in zip(times, subjects, type_of_subjects, teacher_of_subjects, cabinet_of_subjects):
                schedule[w].append({
                    "time": a,
                    "subject": b,
                    "type_of_subject": c,
                    "teacher_of_subject": d,
                    "cabinet_of_subject": e
                })



    return schedule
