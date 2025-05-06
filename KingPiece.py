import pygame
import BasePiece


class King(BasePiece.BasePiece):
    #Function to implement the chess functionality of castling
    def castle(self, TeamLoc, EnemyLoc, PiecePositions):
        Move = []
        PieceLoc = TeamLoc + EnemyLoc
        WhiteKingCastle = True
        WhiteLeftRookCastle = True
        WhiteRightRookCastle = True
        BlackKingCastle = True
        BlackLeftRookCastle = True
        BlackRightRookCastle = True
        KingCheck = False
        squareUnderAttack = self.SquaresUnderAttack(TeamLoc,EnemyLoc,PiecePositions)
        if self.position in squareUnderAttack:
            KingCheck = True
        for i in self.MoveLog:
            if i[2] == "K":
                WhiteKingCastle = False
            if i[2] == "k":
                BlackKingCastle = False
            if i[2] == "R" and i[1] == "0":
                WhiteLeftRookCastle = False
            if i[2] == "R" and i[1] == "7":
                WhiteRightRookCastle = False
            if i[2] == "r" and i[1] == "6":
                BlackLeftRookCastle = False
            if i[2] == "r" and i[1] == "3":
                BlackRightRookCastle = False
        if self.colour == 0:
            if all(square not in PieceLoc for square in [1, 2, 3]) and WhiteKingCastle and WhiteLeftRookCastle and all(pos not in squareUnderAttack for pos in [1, 2, 3]) and KingCheck == False:
                Move.append(2)
            if all(square not in PieceLoc for square in [5, 6]) and WhiteKingCastle and WhiteRightRookCastle and all(pos not in squareUnderAttack for pos in [5,6]) and KingCheck == False:
                Move.append(6)
        if self.colour == 1:
            if all(square not in PieceLoc for square in [57, 58, 59]) and BlackKingCastle and BlackLeftRookCastle and all(pos not in squareUnderAttack for pos in [57, 58, 59]) and KingCheck == False:
                Move.append(58)
            if all(square not in PieceLoc for square in [61, 62]) and BlackKingCastle and BlackRightRookCastle and all(pos not in squareUnderAttack for pos in [61,62]) and KingCheck == False:
                Move.append(62)
        return Move

    #Function to define how the king can move
    def pieceMovement(self, TeamLoc, EnemyLoc, InitialPositionString):
        Moves = []
        directions = [8, -8, 1, -1, 9, -9, 7, -7]
        for direction in directions:
            for i in range(1, 2):
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
        Moves += self.castle(TeamLoc,EnemyLoc, InitialPositionString)
        Moves = [L for L in Moves if self.Legalsquares(InitialPositionString, L)]
        return Moves

    #Function to place the king on the board
    def draw(self):
        X, Y = (self.ConvertNumberToDimension(self.position, self.dimension))
        image = pygame.image.load("Chess_klt60.png" if self.colour == 0 else "Chess_kdt60.png").convert_alpha()
        image = pygame.transform.scale(image, (self.dimension / 8, self.dimension / 8))
        self.screen.blit(image, (X, Y))



