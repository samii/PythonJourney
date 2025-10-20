#!/bin/python3

import  sys
class stack:
    def __init__(self):
        self.stack=[]

    def push_in_stack(self,add_item=''):
        if add_item != '' :
            self.stack.append(add_item)
        else:
            print('you missed sending any element')
    
    def pop_from_stack(self):
        print('Popping an element from stack')
        del self.stack[0]

    def show_stack(self):
        print('stack contents :'+str(self.stack))
        print('length of stack :'+str(len(self.stack)))

if __name__ == '__main__':

    stk=stack()
    stk.push_in_stack(2)
    stk.show_stack()
    stk.push_in_stack(4)
    stk.show_stack()
    stk.push_in_stack(6)
    stk.show_stack()

    stk.push_in_stack(8)
    stk.show_stack()
    stk.push_in_stack(10)
    stk.show_stack()
    stk.pop_from_stack()
    stk.show_stack()
    stk.pop_from_stack()
    stk.show_stack()
    stk.pop_from_stack()
    stk.push_in_stack()
    stk.show_stack()




