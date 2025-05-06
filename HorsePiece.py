import pygame
import BasePiece

class Horse(BasePiece.BasePiece):

    #Function to define how the horse can move
    def pieceMovement(self, TeamLoc, EnemyLoc, InitialPositionString):
        Moves = []
        directions = [-17, -15, -10, -6, 6, 10, 15, 17]
        for direction in directions:
            for i in range(1, 2):
                target = self.position + direction * i
                start_row = self.position // 8
                target_row = target // 8
                row_diff = abs(target_row - start_row)
                if target < 0 or target > 63:
                    break
                if direction in [17,15,-17,-15] and row_diff != 2:
                    break
                if direction in [-6,-10,6,10] and row_diff != 1:
                    break
                if target in TeamLoc:
                    break
                Moves.append(target)
                if target in EnemyLoc:
                    break
        Moves = [L for L in Moves if self.Legalsquares( InitialPositionString, L)]
        return Moves

    #Function to place the horse on the board
    def draw(self):
        X, Y = (self.ConvertNumberToDimension(self.position, self.dimension))
        image = pygame.image.load("Chess_nlt60.png" if self.colour == 0 else "Chess_ndt60.png").convert_alpha()
        image = pygame.transform.scale(image,(self.dimension/8,self.dimension/8))
        self.screen.blit(image, (X, Y))