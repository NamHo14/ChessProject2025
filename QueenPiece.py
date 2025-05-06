import pygame
import BasePiece


class Queen(BasePiece.BasePiece):
    #Function to define how the queen can move
    def pieceMovement(self, TeamLoc, EnemyLoc, InitialPositionString):
        Moves = []
        directions = [8, -8, 1, -1, 9, -9, 7, -7]
        for direction in directions:
            for i in range(1, 8):
                target = self.position + direction * i
                start_row = self.position // 8
                target_row = target // 8
                row_diff = abs(target_row - start_row)
                if target < 0 or target > 63:
                    break
                if direction in [7, -7, 9, -9] and row_diff != i:
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
        Moves = [L for L in Moves if self.Legalsquares( InitialPositionString, L)]
        return Moves

    #Function to place the queen on the board
    def draw(self):
        X, Y = (self.ConvertNumberToDimension(self.position, self.dimension))
        image = pygame.image.load("Chess_qlt60.png" if self.colour == 0 else "Chess_qdt60.png").convert_alpha()
        image = pygame.transform.scale(image,(self.dimension/8,self.dimension/8))
        self.screen.blit(image, (X, Y))