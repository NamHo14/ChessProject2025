import pygame
import BasePiece


class Rook(BasePiece.BasePiece):

    #function to determine possible Moves
    def pieceMovement(self, TeamLoc, EnemyLoc, InitialPositionString):
        Moves = []
        directions = [8, -8, 1, -1]
        for direction in directions:
            for i in range(1, 8):
                target = self.position + (direction * i)
                if target < 0 or target > 63:
                    break
                if direction == 1 and target % 8 == 0:
                    break
                if direction == -1 and target % 8 == 7:
                    break
                if direction == 8 and target // 8 == 0:
                    break
                if direction == -8 and target // 8 == 7:
                    break
                if target in TeamLoc:
                    break
                Moves.append(target)
                if target in EnemyLoc:
                    break
        Moves = [L for L in Moves if self.Legalsquares(InitialPositionString, L)]
        return Moves

    #Function to place the rook on the board
    def draw(self):
        X, Y = (self.ConvertNumberToDimension(self.position, self.dimension))
        image = pygame.image.load("Chess_rlt60.png" if self.colour == 0 else "Chess_rdt60.png").convert_alpha()
        image = pygame.transform.scale(image,(self.dimension/8,self.dimension/8))
        self.screen.blit(image, (X, Y))

