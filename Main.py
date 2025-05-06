
import pygame
import Board
import Convert
import ChessEngine

dimension = 15 * 32
pygame.display.set_caption('Chess Game')
pygame.mixer.init()
pygame.init()
size = (dimension, dimension)
screen = pygame.display.set_mode(size)


clock= pygame.time.Clock()
Board = Board.InitialBoard(dimension,screen)
BillyBob = ChessEngine.MrBot(dimension,screen)
MoveSound = pygame.mixer.Sound("move-self.mp3")

WhitePiece = "RHBQKP"
BlackPiece = "rhbqkp"
MoveLog = []
Message = ""
PossibleMoves = 1
OpponentOptions = True
PositionString = "RHBQKB0RPPPPPPPP00000H00000000000000000000000000pppppppprhbqkbhr"
mouse_held_down = run = Promotion = EndScreen = Robot = False
PiecePressed = WhiteKing = BlackKing = None
Turn = OptionScreenClick = 0
while not run:
    LocationB = []  #Square number of black pieces
    LocationW = []  #Square number of white pieces
    pos = pygame.mouse.get_pos() #Position of mouse

    #Looping through the PositionString and appending square number of White and Black pieces into LocationW and LocationB
    for i in range(len(PositionString)):
        if PositionString[i] in WhitePiece:
            LocationW.append(i)
        if PositionString[i] in BlackPiece:
            LocationB.append(i)

    #Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

        #if button is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN and not mouse_held_down:
            pos = pygame.mouse.get_pos()
            position = int((7 - (pos[1] // (dimension/8))) * 8 + (pos[0] // (dimension/8)))

            if EndScreen == False and OpponentOptions == False:
                #Promotion select
                if Promotion == True:
                    PositionString, Promotion, Turn = Board.PromotionSelect(position,MoveLog,PositionString,Turn)

                #selecting Piece
                if PiecePressed is None:
                    for i in range(len(PositionString)):
                        if (PositionString[i] in WhitePiece) and Turn == 0 :
                            if i == position:
                                OriginalPosition = i
                                PiecePressed = Convert.ConvertLetterToPieceType(PositionString[i], i, dimension, screen, MoveLog)
                        elif (PositionString[i] in BlackPiece) and Turn == 1:
                            if i == position:
                                OriginalPosition = i
                                PiecePressed = Convert.ConvertLetterToPieceType(PositionString[i], i, dimension, screen, MoveLog)

                    mouse_held_down = True

                #Move Piece
                else:
                    if PiecePressed.colour == 0 and Promotion == False:
                        if position in PiecePressed.pieceMovement(LocationW, LocationB,PositionString):
                            for i in range(len(PositionString)):
                                if i == position:
                                    PositionString = PositionString[:i] + PositionString[OriginalPosition] + PositionString[i+1:]
                                    CurrentMove = str(OriginalPosition).zfill(2) + PositionString[i] + str(i).zfill(2)
                                    MoveSound.play()

                            PositionString, MoveLog = Board.MovingPiece(PositionString, CurrentMove, MoveLog,1)
                            Promotion = Board.Promotion(PositionString)
                            PiecePressed = None
                            mouse_held_down = True
                            if Promotion == False:
                                Turn = 1

                        else:
                            PiecePressed = None
                            mouse_held_down = True

                    elif PiecePressed.colour == 1 and Promotion == False:
                        if position in PiecePressed.pieceMovement(LocationB, LocationW,PositionString):
                            for i in range(len(PositionString)):
                                if i == position:
                                    PositionString = PositionString[:i] + PositionString[OriginalPosition] + PositionString[i+1:]
                                    CurrentMove = str(OriginalPosition).zfill(2) + PositionString[i] + str(i).zfill(2)
                                    MoveSound.play()
                            PositionString, MoveLog = Board.MovingPiece(PositionString, CurrentMove, MoveLog,1)

                            Promotion = Board.Promotion(PositionString)

                            PiecePressed = None
                            mouse_held_down = True
                            if Promotion == False:
                                Turn = 0

                        else:
                            PiecePressed = None
                            mouse_held_down = True
        #mouse release
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held_down = False


    if PiecePressed != None:
        if PiecePressed.colour == 0 and Promotion == False:
            PiecePressed.drawOption(screen,PiecePressed.pieceMovement(LocationW, LocationB,PositionString))

        if PiecePressed.colour == 1 and Promotion == False:
            PiecePressed.drawOption(screen, PiecePressed.pieceMovement(LocationB, LocationW,PositionString))

    for i in range(len(PositionString)):
        piece = Convert.ConvertLetterToPieceType(PositionString[i], i, dimension, screen, MoveLog)
        if (piece != None):
            piece.draw()

    #Draw promotion if needed
    Board.DrawPromotion(PositionString, screen)

    #endscreen
    if EndScreen == True:
        if Board.Endscreen(Message, event):
            EndScreen = False
            Turn = 0
            MoveLog = []
            PossibleMoves = 1
            OpponentOptions = True
            OptionScreenClick = pygame.time.get_ticks()

    #Option select screen
    if OpponentOptions == True:
        PositionString = "RHBQKBHRPPPPPPPP00000000000000000000000000000000pppppppprhbqkbhr"
        if pygame.time.get_ticks() - OptionScreenClick >= 200:
            Option = Board.OptionScreen(event)
            Turn = 0
            MoveLog = []
            PossibleMoves = 1
            match Option:
                case 1:
                    Robot = False
                    OpponentOptions = False
                case 2:
                    Robot = True
                    OpponentOptions = False
                    Depth = 2

    # Check for game over
    if EndScreen ==False:
        EndScreen, Message = Convert.GameOver(PositionString, MoveLog, WhitePiece, BlackPiece,Turn,dimension,screen)

    pygame.display.update()

    #Robot move
    if Turn == 1 and Robot == True:
        EndScreen, Message = Convert.GameOver(PositionString, MoveLog, WhitePiece, BlackPiece, Turn, dimension, screen)
        Instruction = BillyBob.BestPlayToMake2(PositionString, 1,MoveLog,Depth)[1]

        if Instruction != None:
            PositionString = Board.MovingPiece(PositionString, Instruction, MoveLog, 1)[0]
            MoveSound.play()
            if "p" in PositionString[0:8]:
                PawnLocation = PositionString.index("p")
                PositionString = PositionString[:PawnLocation] + "q" + PositionString[PawnLocation + 1:]
        Turn = 0

    # Draw the board
    Board.DrawBoard(screen ,dimension)
    clock.tick(200)

