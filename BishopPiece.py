import pygame
import BasePiece

class Bishop(BasePiece.BasePiece):

    #Function to define how the bishop can move
    def pieceMovement(self, TeamLoc, EnemyLoc, InitialPositionString):
        Moves = []
        directions = [9, -9, 7, -7]

        for direction in directions:
            for i in range(1, 8):
                target = self.position + direction * i

                if target < 0 or target > 63:
                    break

                start_row = self.position // 8
                target_row = target // 8
                row_diff = abs(target_row - start_row)

                if direction in [7, -7, 9, -9] and row_diff != i:
                    break

                if target in TeamLoc:
                    break

                Moves.append(target)

                if target in EnemyLoc:
                    break

        Moves = [L for L in Moves if self.Legalsquares(InitialPositionString, L)]
        return Moves

    #Function to place the bishop on the board
    def draw(self):
        X,Y = (self.ConvertNumberToDimension(self.position, self.dimension))

        image = pygame.image.load("Chess_blt60.png" if self.colour == 0 else "Chess_bdt60.png").convert_alpha()

        image = pygame.transform.scale(image, (self.dimension/8, self.dimension/8))

        self.screen.blit(image, (X, Y))

