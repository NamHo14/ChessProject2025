import pygame
import Boards

class BasePiece:
    def __init__(self, screen, position, colour, dimension, MoveLog):
        self.screen = screen
        self.position = position
        self.colour = colour
        self.dimension = dimension
        self.MoveLog = MoveLog

    def pieceMovement(self):
        pass

    def draw(self):
        pass

    #Function to convert each numbered square to coordinates
    def ConvertNumberToDimension(self, SquareNumber, dimension):
        x = SquareNumber % 8 * dimension / 8
        y = (7 - SquareNumber // 8) * dimension / 8
        return x, y

    #Function to highlight the square each piece can move to
    def drawOption(self,screen,Moves):
        for i in range(len(Moves)):
            Square = Moves[i]
            X = (self.ConvertNumberToDimension(Square, self.dimension))[0]
            Y = (self.ConvertNumberToDimension(Square, self.dimension))[1]

            pygame.draw.rect(screen, (255, 255, 255), [X, Y - (1*self.dimension)/480, (61*self.dimension)/480, (2*self.dimension)/480])
            pygame.draw.rect(screen, (255, 255, 255), [X - (1*self.dimension)/480, Y, (2*self.dimension)/480, (61*self.dimension)/480])
            pygame.draw.rect(screen, (255, 255, 255), [X + (59*self.dimension)/480, Y, (2*self.dimension)/480, (61*self.dimension)/480])
            pygame.draw.rect(screen, (255, 255, 255), [X, Y + (59*self.dimension)/480, (61*self.dimension)/480, (2*self.dimension)/480])

        X = (self.ConvertNumberToDimension(self.position, self.dimension))[0]
        Y = (self.ConvertNumberToDimension(self.position, self.dimension))[1]

        pygame.draw.rect(screen, (255, 255, 255),[X, Y - (1 * self.dimension) / 480, (61 * self.dimension) / 480, (2 * self.dimension) / 480])
        pygame.draw.rect(screen, (255, 255, 255),[X - (1 * self.dimension) / 480, Y, (2 * self.dimension) / 480, (61 * self.dimension) / 480])
        pygame.draw.rect(screen, (255, 255, 255),[X + (59 * self.dimension) / 480, Y, (2 * self.dimension) / 480, (61 * self.dimension) / 480])
        pygame.draw.rect(screen, (255, 255, 255),[X, Y + (59 * self.dimension) / 480, (61 * self.dimension) / 480, (2 * self.dimension) / 480])

    #Function to check if a move is legal or not
    def Legalsquares(self, PiecePositions, NewPosition):
        TeamLoc = []
        EnemyLoc = []
        WhitePiece = "RHBQKP"
        BlackPiece = "rhbqkp"

        Board1 = Boards.InitialBoard(self.dimension,self.screen)
        type = PiecePositions[self.position]
        stringMove = str(self.position).zfill(2) + type + str(NewPosition).zfill(2)
        BoardAfter = Board1.MovingPiece(PiecePositions, stringMove, self.MoveLog,0)[0]

        if self.colour == 0:
            for i in range(len(BoardAfter)):
                if (BoardAfter[i] in WhitePiece):
                    TeamLoc.append(i)
                if (BoardAfter[i] in BlackPiece):
                    EnemyLoc.append(i)

        elif self.colour == 1:
            for i in range(len(BoardAfter)):
                if (BoardAfter[i] in WhitePiece):
                    EnemyLoc.append(i)
                if (BoardAfter[i] in BlackPiece):
                    TeamLoc.append(i)
        squareUnderAttack = self.SquaresUnderAttack(TeamLoc, EnemyLoc, BoardAfter)

        if self.colour == 0:
            KingLoction = BoardAfter.find("K")
            if (KingLoction in squareUnderAttack):
                return False

        elif self.colour == 1:
            KingLoction = BoardAfter.find("k")
            if (KingLoction in squareUnderAttack):
                return False
        return True

    #Function to identify all squares that the opposing team piece are attacking
    def SquaresUnderAttack(self,TeamLoc, EnemyLoc, PiecePositions):
        SquaresUnderAttack = []

        for i in range(len(PiecePositions)):
            if ((PiecePositions[i] == "K" or PiecePositions[i] == "k") and i in EnemyLoc):
                Moves = []
                directions = [8, -8, 1, -1, 9, -9, 7, -7]
                for direction in directions:
                    for P in range(1, 2):
                        target = i + direction * P
                        start_row = i // 8
                        target_row = target // 8
                        row_diff = abs(target_row - start_row)

                        if target < 0 or target > 63:
                            break

                        if direction in [7, -7, 9, -9] and row_diff != P:
                            break

                        if direction == 1 and target % 8 == 0:
                            break

                        if direction == -1 and target % 8 == 7:
                            break

                        if direction == 8 and target // 8 == 0:
                            break

                        if direction == -8 and target // 8 == 7:
                            break

                        if target in EnemyLoc:
                            break

                        Moves.append([target])

                        if target in TeamLoc:
                            break

                Moves = list(set([item for sublist in Moves for item in sublist]))
                SquaresUnderAttack.append(Moves)

            elif PiecePositions[i] == "p" and i in EnemyLoc:
                        if (i % 8 != 7) and i - 7 not in EnemyLoc:
                            SquaresUnderAttack.append([i - 7])
                        if (i % 8 != 0) and i - 9 not in EnemyLoc:
                            SquaresUnderAttack.append([i - 9])

            elif PiecePositions[i] == "P" and i in EnemyLoc:
                        if (i % 8 != 0) and i + 7 not in EnemyLoc:
                            SquaresUnderAttack.append([i + 7])
                        if (i % 8 != 7) and i + 9 not in EnemyLoc:
                            SquaresUnderAttack.append([i + 9])

            elif (PiecePositions[i] == "Q" or PiecePositions[i] == "q") and i in EnemyLoc:
                Moves = []
                directions = [8, -8, 1, -1, 9, -9, 7, -7]
                for direction in directions:
                    for P in range(1, 8):
                        target = i + direction * P
                        start_row = i // 8
                        target_row = target // 8
                        row_diff = abs(target_row - start_row)

                        if target < 0 or target > 63:
                            break

                        if direction in [7, -7, 9, -9] and row_diff != P:
                            break

                        if direction == 1 and target % 8 == 0:
                            break

                        if direction == -1 and target % 8 == 7:
                            break

                        if direction == 8 and target // 8 == 0:
                            break

                        if direction == -8 and target // 8 == 7:
                            break

                        if target in EnemyLoc:
                            break

                        Moves.append([target])

                        if target in TeamLoc:
                            break
                Moves = list(set([item for sublist in Moves for item in sublist]))
                SquaresUnderAttack.append(Moves)

            elif ((PiecePositions[i] == "R" or PiecePositions[i] == "r") and i in EnemyLoc):
                Moves = []
                directions = [8, -8, 1, -1]
                for direction in directions:
                    for P in range(1, 8):
                        target = i + direction * P

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

                        if target in EnemyLoc:
                            break

                        Moves.append([target])

                        if target in TeamLoc:
                            break
                Moves = list(set([item for sublist in Moves for item in sublist]))
                SquaresUnderAttack.append(Moves)

            elif ((PiecePositions[i] == "B" or PiecePositions[i] == "b") and i in EnemyLoc):
                Moves = []
                directions = [9, -9, 7, -7]
                for direction in directions:
                    for P in range(1, 8):
                        target = i + direction * P

                        if target < 0 or target > 63:
                            break

                        start_row = i // 8
                        target_row = target // 8
                        row_diff = abs(target_row - start_row)

                        if direction in [7, -7, 9, -9] and row_diff != P:
                            break

                        if target in EnemyLoc:
                            break

                        Moves.append([target])

                        if target in TeamLoc:
                            break

                Moves = list(set([item for sublist in Moves for item in sublist]))
                SquaresUnderAttack.append(Moves)

            elif ((PiecePositions[i] == "H" or PiecePositions[i] == "h") and i in EnemyLoc):
                Moves = []
                directions = [-17, -15, -10, -6, 6, 10, 15, 17]
                for direction in directions:
                    for P in range(1, 2):
                        target = i + direction * P
                        start_row = i // 8
                        target_row = target // 8
                        row_diff = abs(target_row - start_row)

                        if target < 0 or target > 63:
                            break

                        if direction in [17,15,-17,-15] and row_diff != 2:
                            break

                        if direction in [-6, -10, 6, 10] and row_diff != 1:
                            break

                        if target in EnemyLoc:
                            break

                        Moves.append([target])

                        if target in TeamLoc:
                            break

                Moves = list(set([item for sublist in Moves for item in sublist]))
                SquaresUnderAttack.append(Moves)

        SquaresUnderAttack = list(set([item for sublist in SquaresUnderAttack for item in sublist]))
        return SquaresUnderAttack


