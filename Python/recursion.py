class Solution(object):
    def exist(self, board, word):
        
        
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
    #Need Size of Board. 
        board_size = len(board)
    
    
        #Need size of Array inside Array.

        # convert word into char.
        index=0
        


        for x in range(board_size):
            for i in range (len(board[x])):
                                if board[x][i] == word[index] and self.search(board,x,i, index,word) :
                                        return True
        return False
                                
    
    
    
    def search(self, board, x, i , index, word):

        if index == len(word):
            return True
        if x >= len(board) or x < 0 or i >= len(board[x]) or i < 0 or board[x][i] != word[index]:
            return False;
        
        holder = board[x][i]
        
        board[x][i] = "*"
        found = self.search(board,x-1,i,index+1,word) or self.search(board,x+1,i,index+1,word) or self.search(board,x,i-1,index+1,word) or self.search(board,x,i+1,index+1,word)
        board[x][i] =holder
        return found

        
        
        
    
    
    
    #Check if next letter matches following char of 'Word'
    
    #If it doesn't match drop to the next array with same position.
    #If Match. check the previous if it matches. 
        #If it matches check if we are at the end . if yes drop array to next array.
        
    