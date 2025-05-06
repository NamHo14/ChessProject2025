import pygame
import Convert
import Boards
import KingPiece

class MrBot:
    def __init__(self, dimension = 480, screen = pygame.display.set_mode((480,480))):
        self.dimension = dimension
        self.screen = screen
        self.Board1 = Boards.InitialBoard(self.dimension, self.screen)

    #Function to determine the worth of a piece depending on the type and the position on the board
    def RelativePieceValues(self, PieceType, index):
        match PieceType:
            case "R":
                WhiteRook = ("+00+00+00+05+05+00+00+00"
                             "-05+00+00+00+00+00+00-05"
                             "-05+00+00+00+00+00+00-05"
                             "-05+00+00+00+00+00+00-05"
                             "-05+00+00+00+00+00+00-05"
                             "-05+00+00+00+00+00+00-05"
                             "+05+10+10+10+10+10+10+05"
                             "+00+00+00+00+00+00+00+00")
                displacement = int(WhiteRook[index * 3: index * 3 + 3])/10
                return (5 + displacement)
            case "H":
                WhiteKnight = ("-50-40-30-30-30-30-40-50"
                               "-40-20+00+05+05+00-20-40"
                               "-30-05+10+15+15+10+05-30"
                               "-30+00+15+20+20+15-00-30"
                               "-30+05+15+20+20+15+05-30"
                               "-30+00+10+15+15+10+00-30"
                               "-40-20+00+00+00+00-20-40"
                               "-50-40-30-30-30-30-40-50")
                displacement = int(WhiteKnight[index * 3: index * 3 + 3])/10
                return (3 + displacement)
            case "B":
                WhiteBishop = ("-20-10-10-10-10-10-10-20"
                               "-10+05+00+00+00+00+05-10"
                               "-10+10+10+10+10+10+10-10"
                               "-10+00+10+10+10+10+00-10"
                               "-10+05+05+10+10+05+05-10"
                               "-10+05+05+10+10+05+05-10"
                               "-10+00+00+00+00+00+00-10"
                               "-20-10-10-10-10-10-10-20")

                displacement = int(WhiteBishop[index * 3: index * 3 + 3])/10
                return (3 + displacement)
            case "Q":
                WhiteQueen = ("-20-10-10-05-05-10-10-20"
                              "-10+00+05+00+00+00+00-10"
                              "-10+05+05+05+05+05+00-10"
                              "+00+00+05+05+05+05+00-05"
                              "-05+00+05+05+05+05+00-05"
                              "-10+00+05+05+05+05+00-10"
                              "-10+00+00+00+00+00+00-10"
                              "-20-10-10-05-05-10-10-20")
                displacement = int(WhiteQueen[index * 3: index * 3 + 3]) / 10
                return (9 + displacement)
            case "K":
                WhiteKing  = ("+20+30+10+00+00+10+30+20"
                              "+20+20+00+00+00+00+20+20"
                              "-10-20-20-20-20-20-20-10"
                              "-20-30-30-40-40-30-30-20"
                              "-30-40-40-50-50-40-40-30"
                              "-30-40-40-50-50-40-40-30"
                              "-30-40-40-50-50-40-40-30"
                              "-30-40-40-50-50-40-40-30")
                displacement = int(WhiteKing[index * 3: index * 3 + 3]) / 10
                return (10000 + displacement)
            case "P":
                WhitePawn = ("+00+00+00+00+00+00+00+00"
                             "+05+10+10-20-20+10+10+05"
                             "+05-05-10+00+00-10+05+05"
                             "+00+00+00+20+20+00+00+00"
                             "+05+05+10+25+25+10+05+05"
                             "+10+10+20+30+30+20+10+10"
                             "+50+50+50+50+50+50+50+50"
                             "+00+00+00+00+00+00+00+00")
                displacement = int(WhitePawn[index * 3: index * 3 + 3]) / 10
                return (1 + displacement)
            case "r":
                BlackRook = ("+00+00+00+00+00+00+00+00"
                             "+05+10+10+10+10+10+10+05"
                             "-05+00+00+00+00+00+00-05"
                             "-05+00+00+00+00+00+00-05"
                             "-05+00+00+00+00+00+00-05"
                             "-05+00+00+00+00+00+00-05"
                             "-05+00+00+00+00+00+00-05"
                             "+00+00+00+00+00+00+00+00")
                displacement = int(BlackRook[index * 3: index * 3 + 3]) / 10
                return -(5 + displacement)
            case "h":
                BlackKnight = ("-50-40-30-30-30-30-40-50"
                               "-40-20+00+00+00+00-20-40"
                               "-30+00+10+15+15+10+00-30"
                               "-30+05+15+20+20+15+05-30"
                               "-30+00+15+20+20+15+00-30"
                               "-30+05+10+15+15+10+05-30"
                               "-40-20+00+05+05+00-20-40"
                               "-50-40-30-30-30-30-40-50")
                displacement = int(BlackKnight[index * 3: index * 3 + 3]) / 10
                return -(3 + displacement)
            case "b":
                BlackBishop = ("-20-10-10-10-10-10-10-20"
                               "-10+00+00+00+00+00+00-10"
                               "-10+00+05+10+10+05+00-10"
                               "-10+05+05+10+10+05+05-10"
                               "-10+00+10+10+10+10+00-10"
                               "-10+10+10+10+10+10+10-10"
                               "-10+05+00+00+00+00+05-10"
                               "-20-10-10-10-10-10-10-20")
                displacement = int((BlackBishop[index * 3: index * 3 + 3])) / 10
                return -(3 + displacement)
            case "q":
                BlackQueen = ("-20-10-10-05-05-10-10-20"
                              "-10+00+00+00+00+00+00-10"
                              "-10+00+05+05+05+05+00-10"
                              "-05+00+05+05+05+05+00-05"
                              "+00+00+05+05+05+05+00-05"
                              "-10+05+05+05+05+05+00-10"
                              "-10+00+05+00+00+00+00-10"
                              "-20-10-10-05-05-10-10-20")
                displacement = int((BlackQueen[index * 3: index * 3 + 3])) / 10
                return -(9 + displacement)
            case "k":
                BlackKing = ("-30-40-40-50-50-40-40-30"
                             "-30-40-40-50-50-40-40-30"
                             "-30-40-40-50-50-40-40-30"
                             "-30-40-40-50-50-40-40-30"
                             "-20-30-30-40-40-30-30-20"
                             "-10-20-20-20-20-20-20-10"
                             "+20+20+00+00+00+00+20+20"
                             "+20+30+10+00+00+10+30+20")
                displacement = int((BlackKing[index * 3: index * 3 + 3])) / 10
                return -(10000 + displacement)
            case "p":
                BlackPawn = ("+00+00+00+00+00+00+00+00"
                             "+50+50+50+50+50+50+50+50"
                             "+10+10+20+30+30+20+10+10"
                             "+05+05+10+25+25+10+05+05"
                             "+00+00+00+20+20+00+00+00"
                             "+05-05-10+00+00-10-05+05"
                             "+05+10+10-20-20+10+10+05"
                             "+00+00+00+00+00+00+00+00")
                displacement = int((BlackPawn[index * 3: index * 3 + 3])) / 10
                return -(1 + displacement)
        return 0

    #Function to evaluate the board and return a evaluation value
    def BoardEvaluation(self, BoardPosition):
        EvaluationTotal = 0
        for i in range(len(BoardPosition)):
            EvaluationTotal  = EvaluationTotal + self.RelativePieceValues(BoardPosition[i],i)

        return EvaluationTotal

    #Function to determine the BestPlay to make
    def BestPlayToMake2(self, BoardPosition, colour, MoveLog = [], depth=3, alpha = -99999, beta = 99999):
        if depth ==0:
            return self.BoardEvaluation(BoardPosition), None
        TeamLocation = []
        EnemyLocation = []
        if (colour == 0):
            Team = "RHBQKP"
        else:
            Team = "rhbqkp"

        for i in range(len(BoardPosition)):
            if (BoardPosition[i] in Team):
                TeamLocation.append(i)
            elif (BoardPosition[i] != "0"):
                EnemyLocation.append(i)

        TotalPossibleMoves = []
        for i in range(len(BoardPosition)):
            if BoardPosition[i] in Team:
                Piece = Convert.ConvertLetterToPieceType(BoardPosition[i], i, self.dimension, self.screen, MoveLog)
                Moves = Piece.pieceMovement(TeamLocation, EnemyLocation, BoardPosition)
                #print(Moves)
                for j in Moves:
                    PossibleMoves = str(i).zfill(2) + BoardPosition[i] + str(j).zfill(2)
                    TotalPossibleMoves.append(PossibleMoves)

        if colour == 0:
            MaxMoveEvaluation = -99999
            bestMove = None
            for K in TotalPossibleMoves:
                BoardPositionNew = self.Board1.MovingPiece(BoardPosition, K, MoveLog, 0)[0]
                if "p" in BoardPositionNew[0:8]:
                    PawnLocation = BoardPositionNew.index("p")
                    BoardPositionNew = BoardPositionNew[:PawnLocation] + "q" + BoardPositionNew[PawnLocation + 1:]
                if "P" in BoardPosition[56:64]:
                    PawnLocation = BoardPositionNew.index("P")
                    BoardPositionNew = BoardPositionNew[:PawnLocation] + "Q" + BoardPositionNew[PawnLocation + 1:]

                MoveLogNew = MoveLog + [K]
                MoveEvaluation = self.BestPlayToMake2(BoardPositionNew,colour^1,MoveLogNew,depth-1)[0]
                if MoveEvaluation>MaxMoveEvaluation:
                    MaxMoveEvaluation = MoveEvaluation
                    bestMove = K
                MaxMoveEvaluation = max(MaxMoveEvaluation, MoveEvaluation)
                alpha = max(alpha, MoveEvaluation)
                if beta <=alpha:
                    break
            return (MaxMoveEvaluation,bestMove)

        else:
            MinMoveEvaluation = 99999
            bestMove = None
            for K in TotalPossibleMoves:
                BoardPositionNew = self.Board1.MovingPiece(BoardPosition, K, MoveLog, 0)[0]
                MoveLogNew = MoveLog + [K]
                if ("p" in BoardPositionNew[0:8]):
                    PawnLocation = BoardPositionNew.index("p")
                    BoardPositionNew = BoardPositionNew[:PawnLocation] + "q" + BoardPositionNew[PawnLocation + 1:]
                if ("P" in BoardPositionNew[56:64]):
                    PawnLocation = BoardPositionNew.index("P")
                    BoardPositionNew = BoardPositionNew[:PawnLocation] + "Q" + BoardPositionNew[PawnLocation + 1:]

                MoveEvaluation = self.BestPlayToMake2(BoardPositionNew, colour^1, MoveLogNew, depth-1)[0]

                if MoveEvaluation<MinMoveEvaluation:
                    MinMoveEvaluation = MoveEvaluation
                    bestMove = K

                MinMoveEvaluation = min(MinMoveEvaluation, MoveEvaluation)
                beta = min(beta, MinMoveEvaluation)
                if beta <=alpha:
                    break
            return (MinMoveEvaluation, bestMove)


