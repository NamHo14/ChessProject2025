import pygame
import BasePiece


class Pawn(BasePiece.BasePiece):

    #Function to define the chess functionality of En Passant
    def EnPassant(self):
        Move = []
        if self.MoveLog:
            LastMove = self.MoveLog[len(self.MoveLog)-1]
            if self.colour == 0:
                if (int(LastMove[0:2]) - int(LastMove[3:5]) == 16) and (LastMove[2] == "p") and ((self.position == int(LastMove[3:5]) - 1) or self.position == (int(LastMove[3:5]) + 1)):
                    Move.append((int(LastMove[3:5])+8))
            if self.colour == 1:
                if int(LastMove[0:2]) - int(LastMove[3:5]) == -16 and LastMove[2] == "P" and (self.position == int(LastMove[3:5])-1 or self.position == int(LastMove[3:5])+1):
                    Move.append((int(LastMove[3:5])-8))
        return Move

    #Function to allow a pawn to move diagonally to eat the opposing team's pawn
    def PawnEatPawn(self, EnemyLoc):
        Moves = []
        if self.colour == 0:
            for i in EnemyLoc:
                if i == self.position + 7 and self.position%8 != 0:
                    Moves.append(self.position + 7)
                if i == self.position + 9 and self.position%8 != 7:
                    Moves.append(self.position + 9)
        if self.colour == 1:
            for i in EnemyLoc:
                if i == self.position - 7 and self.position%8 != 7:
                    Moves.append(self.position - 7)
                if i == self.position - 9 and self.position%8 != 0:
                    Moves.append(self.position - 9)
        return Moves

    #Function to define how the pawn can move
    def pieceMovement(self, TeamLoc, EnemyLoc, InitialPositionString):
        Moves = []
        if self.colour == 0:
            directions = [8, 16]
            for direction in directions:
                for i in range (1,2):
                    target = self.position + direction * i
                    if target < 0 or target > 63:
                        break
                    if direction in [16] and (self.position//8 != 1 or self.position+8 in TeamLoc or self.position+8 in EnemyLoc) :
                        break
                    if target in TeamLoc:
                        break
                    if target in EnemyLoc:
                        break
                    Moves.append(target)

        if self.colour == 1:
            directions = [-8, -16]
            for direction in directions:
                for i in range(1, 2):
                    target = self.position + direction * i
                    if target < 0 or target > 63:
                        break
                    if direction in [-16] and (self.position // 8 != 6 or self.position-8 in TeamLoc or self.position-8 in EnemyLoc):
                        break
                    if target in TeamLoc:
                        break
                    if target in EnemyLoc:
                        break
                    Moves.append(target)

        Moves = Moves + self.PawnEatPawn(EnemyLoc) + self.EnPassant()
        Moves = [L for L in Moves if self.Legalsquares( InitialPositionString, L)]
        return Moves

    #Function to place the pawn on the board
    def draw(self):
        X, Y = (self.ConvertNumberToDimension(self.position, self.dimension))
        image = pygame.image.load("Chess_plt60.png" if self.colour == 0 else "Chess_pdt60.png").convert_alpha()
        image = pygame.transform.scale(image,(self.dimension/8,self.dimension/8))
        self.screen.blit(image, (X, Y))