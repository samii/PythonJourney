"""Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having 
the second lowest grade."""






if __name__ == '__main__':
        records=[]
        score_list=[]
        for i in range(int(input())):
          name1 = input()
          score = float(input())
          records.append([name1,score])
          score_list.append(score)
        #print (score_list)
        max0=0.0
        for i in range(len(score_list)):
            for j in range(i,len(score_list)):
             if(score_list[j] > score_list[i]):
                 max0 = score_list[i]
                 score_list[i] = score_list[j]
                 score_list[j] = max0
        #print (score_list)
        max0 = score_list[len(score_list)-1]
        #print (max0)
        for j in range(len(score_list)-2,0,-1):
                #print (score_list[j])
                if(score_list[j] != max0):
                  max0 = score_list[j]
                  break
        #print (max0)
        slowest=[nam for nam,scr in records if scr == max0]
        #print (slowest)
        slowest.sort()
        print ("\n".join(slowest))
