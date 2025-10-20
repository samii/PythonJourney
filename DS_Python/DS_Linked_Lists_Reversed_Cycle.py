#!/bin/python3

import  sys

class Linked_List:

    def __init__(self):
        self.Head=None
        self.Length=0
        self.Tail=None
    
    def create_new_node(self,add_item,addr):
        return Node(add_item,addr)
    
    def add_n_pos_list(self,add_item,pos=0):
        BefPoin=self.Head
        Pos_Point=0
        Temp=self.Head
        if pos==0:
            if pos>self.Length :
                print('pos is more than its length so it ll be added in front ')

            Nod=self.create_new_node(add_item,self.Head)
            self.Head=Nod
            self.Length+=1
        else:
            while (Temp.addr!=None):
                        BefPoin=Temp
                        Temp=Temp.addr
                        Pos_Point+=1
                        if Pos_Point==pos:
                            break
            if Temp.addr==None and pos>=self.Length :
                Nod=self.create_new_node(add_item,None)
                Temp.addr=Nod
            else:
                Nod=self.create_new_node(add_item,Temp)
                BefPoin.addr=Nod

            self.Length+=1

    def add_list(self,add_item='',pos=0):
        if pos<0:
            pos=self.Length
        if add_item != '':
            self.add_n_pos_list(add_item,pos)
            print('adding a new element in the list ',add_item)
        else:
            print('you missed sending any element')
    
    def del_from_list(self,val='',tail=0):
        Temp=self.Head
        Found=-1
        BefPoin=self.Head
        if self.Length>0 :
            if tail == 1 and self.Length ==1  :
                self.Head=Temp.addr
                val=Temp.value
                del Temp
                Found=1
                print('Found %d & Successfully deleted from end. '%val)
            if tail == 1:
                    while (Temp.addr!=None):
                        BefPoin=Temp
                        Temp=Temp.addr
                    BefPoin.addr=Temp.addr
                    del Temp 
                    Found=1
            else:
                if val!='':
                    if self.Head.value==val :
                        self.Head=Temp.addr
                        del Temp
                        Found=1
                        print('Found %d & Successfully deleted '%val)
                    else:
                         while (Temp!=None):
                            if (Temp.value== val):
                                BefPoin.addr=Temp.addr
                                print('Found %d & Successfully deleted '%val)
                                del Temp
                                Found=1
                                break

                            BefPoin=Temp
                            Temp=Temp.addr
            if Found!=1:
                print ('we couldnt find '+str(val))
            else:
                self.Length-=1

        else:
            print('Linked List is empty.')

    def show_list(self):
        self.navigate_list()
        print('length of Lists :'+str(self.Length))

    def navigate_list(self):
        if self.Head!=None:
            Temp=self.Head
            tail=None
            print('List contents :')
            while (Temp!=None):
                print (Temp.value)
                tail=Temp
                Temp=Temp.addr
            self.Tail=tail
        else:
            print('List is empty!')

    def update_tail_pointer(self):
        self.navigate_list()

        
    def reverse_cycle(self):
        if self.Head==None:
            print('List is empty!')
            return
        self.update_tail_pointer()
        Reverse_head=self.Tail
        Reverse_Tail=self.Head
        Head_Pointer=self.Head
        Next_Head_Pointer=self.Head.addr
        Head_Pointer.addr=None
        Temp=Next_Head_Pointer
        while (Temp!=None):
            Temp=Next_Head_Pointer.addr
            Next_Head_Pointer.addr=Head_Pointer
            Head_Pointer=Next_Head_Pointer
            Next_Head_Pointer=Temp
        self.Head=Reverse_head
        self.Tail=Reverse_Tail





class Node:

    def __init__(self,val='',head=None):
        if val!='':
            self.value=val
            self.addr=head




if __name__ == '__main__':

    stk=Linked_List()
    stk.add_list(2)
    stk.add_list(4)
    stk.add_list(6)
    stk.show_list()
    stk.reverse_cycle()
    stk.show_list()
    stk.reverse_cycle()
    stk.show_list()



    


