import RookPiece
import HorsePiece
import BishopPiece
import KingPiece
import QueenPiece
import PawnPiece

#Function to Create an object for the select piece
def ConvertLetterToPieceType(letter, index, dimension, screen ,MoveLog):
    match letter:
        case "R":
            WhiteRook = RookPiece.Rook(screen, index, 0, dimension, MoveLog)
            return WhiteRook
        case "H":
            WhiteHorse = HorsePiece.Horse(screen, index, 0, dimension, MoveLog)
            return WhiteHorse
        case "B":
            WhiteBishop = BishopPiece.Bishop(screen, index, 0, dimension, MoveLog)
            return WhiteBishop
        case "Q":
            WhiteQueen = QueenPiece.Queen(screen,index, 0, dimension, MoveLog)
            return WhiteQueen
        case "K":
            WhiteKing = KingPiece.King(screen, index, 0, dimension, MoveLog)
            return WhiteKing
        case "P":
            WhitePawn = PawnPiece.Pawn(screen, index, 0, dimension, MoveLog)
            return WhitePawn
        case "r":
            BlackRook = RookPiece.Rook(screen, index, 1, dimension, MoveLog)
            return BlackRook
        case "h":
            BlackHorse = HorsePiece.Horse(screen, index, 1, dimension, MoveLog)
            return BlackHorse
        case "b":
            BlackBishop = BishopPiece.Bishop(screen, index, 1, dimension, MoveLog)
            return BlackBishop
        case "q":
            BlackQueen = QueenPiece.Queen(screen,index, 1, dimension, MoveLog)
            return BlackQueen
        case "k":
            BlackKing = KingPiece.King(screen, index, 1, dimension, MoveLog)
            return BlackKing
        case "p":
            BlackPawn = PawnPiece.Pawn( screen, index, 1, dimension, MoveLog)
            return BlackPawn
    return None

#Function to check if it is game over by Draw or CheckMate
def GameOver(PositionString, MoveLog,WhitePiece, BlackPiece,Turn,dimension,screen):
    PossibleMovesWhite = 1
    PossibleMovesBlack = 1
    TotalBlackMoves = []
    TotalWhiteMoves = []
    LocationW=[]
    LocationB=[]
    #print(PositionString)
    for i in range(len(PositionString)):
        if PositionString[i] in WhitePiece:
            LocationW.append(i)
        if PositionString[i] in BlackPiece:
            LocationB.append(i)
    for i in range(len(PositionString)):
        if Turn == 0:
            if PositionString[i] == "K":
                WhiteKing = ConvertLetterToPieceType(PositionString[i], i, dimension, screen, MoveLog)
            if (PositionString[i] in WhitePiece):
                WhitePieceCombination = ConvertLetterToPieceType(PositionString[i], i, dimension, screen, MoveLog)
                PossibleWhiteMoves = WhitePieceCombination.pieceMovement(LocationW, LocationB, PositionString)
                TotalWhiteMoves.append(PossibleWhiteMoves)
        if Turn == 1:
            if PositionString[i] == "k":
                BlackKing = ConvertLetterToPieceType(PositionString[i], i, dimension, screen, MoveLog)
            if (PositionString[i] in BlackPiece):
                BlackPieceCombination = ConvertLetterToPieceType(PositionString[i], i, dimension, screen, MoveLog)
                PossibleBlackMoves = BlackPieceCombination.pieceMovement(LocationB, LocationW, PositionString)

                TotalBlackMoves.append(PossibleBlackMoves)

    if all(item == [] for item in TotalWhiteMoves):
        PossibleMovesWhite = 0
    if all(item == [] for item in TotalBlackMoves):
        PossibleMovesBlack = 0

    if ((set(PositionString).issubset({"K", "k", "0"})) or ((set(PositionString).issubset({"K", "k", "b", "0"})) and PositionString.count("b") == 1) or (set(PositionString).issubset({"K", "k", "B", "0"}) and PositionString.count("b") == 1) ):
        Message = "DRAW"
        return True, Message
    if Turn == 0:
        if (WhiteKing.position not in WhiteKing.SquaresUnderAttack(LocationW, LocationB, PositionString) and PossibleMovesWhite == 0):
            Message = "DRAW"
            return True, Message
        elif (WhiteKing.position in WhiteKing.SquaresUnderAttack(LocationW, LocationB,PositionString) and PossibleMovesWhite == 0):
            Message = "CHECKMATE BLACK WINS"
            return True, Message
    if Turn == 1:
        if (BlackKing.position not in BlackKing.SquaresUnderAttack(LocationB, LocationW, PositionString) and PossibleMovesBlack == 0):
            Message = "DRAW"
            return True, Message
        if(BlackKing.position in BlackKing.SquaresUnderAttack(LocationB, LocationW, PositionString) and PossibleMovesBlack == 0):
            Message = "CHECKMATE WHITE WINS"
            return True, Message
    return False, ""

