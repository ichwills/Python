class Chess:
    steps = [1,2,3,4,5,6,7,8,9]
    cnt = 0#当前下子有效步数
    rules = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[2,5,8],[3,6,9],[1,4,7]]

    def print_board(self):
        print(f'{self.steps[0]} | {self.steps[1]} | {self.steps[2]}')
        print('-'*9)
        print(f'{self.steps[3]} | {self.steps[4]} | {self.steps[5]}')
        print('-'*9)
        # print(f'{steps[6]}' | f'{steps[7]}' | f'{steps[8]}')
        print('{} | {} | {}'.format(self.steps[6], self.steps[7], self.steps[8]))

    def move(self,pos):
        #pos有效性的判断
        if self.cnt%2==0: #判断步数是奇数还是偶数
            self.steps[pos - 1] = 'o'
        else:
            self.steps[pos - 1] = 'x'
        self.cnt += 1
    def is_win(self):
        #是否要进行输赢判断的判断
        #判断当前是哪方下完
        if self.cnt%2==0:
            ch="x"  #ch代表当前下棋方
        else:
            ch="o"
        #只提取当前方相关信息，进行置换
        new_steps = self.steps[:]
        for i in range(9):
            if new_steps[i] ==ch:
                new_steps[i] =1
            else:
                new_steps[i] =0
        for i in self.rules:
            for j in i:
                total+=j
            if total==3:
                return  True
        return False
    def run(self):
        while(result):#循环结束条件可以考虑result，或者步数
            print('欢迎进入游戏')
            self.print_board()
            pos = input('请o方输入下子的位置(1-9)')#到哪方下子需要判断
            self.move(pos)
            result =self.is_win()
            if result:
                print("淦,你真聪明!!!")
            else: 
                print("算啦你")
chess=Chess()
chess.run()